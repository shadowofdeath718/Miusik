import os
from datetime import datetime
from src import metadata

date_format = "%m-%d-%Y"
datetime_format = "%m-%d-%Y %H:%M"


class Track(object):
    __slots__ = ["__tags", "_scan_valid"]

    def __init__(self, loc):
        """
            parameters:
                loc: must be valid unicode text location
        """
        self.__tags = {}
        self._scan_valid = None
        self.__tags['__loc'] = loc
        self.set_tags()

    def __str__(self):
        # return self.__tags.get('title') + ', ' + self.__tags.get('album') + \
        #     ', ' + self.__tags.get('artist')
        return self.__tags.__str__()

    def get_file_size(self):
        """Return file size in Mb"""
        size = os.path.getsize(self.get_loc())  # it is bytes
        return round(size / 1024.0 / 1024.0, 2)

    def get_loc(self):
        """
            Return location.
        """
        return self.__tags['__loc']

    def get_basedir(self):
        """
            Return folder path of file path
            Ex: file_path = u"D:/Music/It Will Rain.mp3"
            dir_path = u"D:/Music"
        """
        return os.path.dirname(self.get_loc())

    def get_basename(self):
        """
            Return file name
            Ex: file_path = u"D:/Music/It Will Rain.mp3"
            basename = u"It Will Rain.mp3"
        """
        return os.path.basename(self.get_loc())

    def get_tag_raw(self, tag, join=False):
        """
            Get the raw value of a tag.  For non-internal tags, the
            result will always be a list of unicode strings.

            :param tag: The name of the tag to get
            :param join: If True, joins lists of values into a
                single value.
        """
        if tag == '__basename':
            value = self.get_basename()
        elif tag == '__startoffset':  # necessary?
            value = self.__tags.get(tag, 0)
        else:
            value = self.__tags.get(tag)

        if join and value and not tag.startswith('__'):
            return u';'.join(value)

        return value

    def set_tag_raw(self, tag, values):
        """
            Private function for setting tag to __tags
        """
        if tag in ("__loc", "__basedir", "__basename"):
            pass

        if not isinstance(values, list):
            if not tag.startswith("__"):  # internal tags don't have to be lists
                values = [values]
        else:
            # save memory by removing some null values
            [value for value in values if value not in (None, u'')]

        if not values:
            try:
                del self.__tags[tag]
            except KeyError:
                pass
        else:
            self.__tags[tag] = values

    def list_tags(self):
        """
            List all tags in self.__tags.
        """
        return self.__tags.keys() + ['__basename']

    def set_tags(self):
        """
            Reads tags from the file and set for this Track.

            Returns False if unsuccessful, otherwise returns
            Format object from 'src.metadata'.
        """
        try:
            f = metadata.get_format(self.get_loc())
            if f is None:
                self._scan_valid = False
                return False  # not a supported type
            ntags = f.read_all()
            for k, v in ntags.iteritems():
                self.set_tag_raw(k, v)

            # remove tags that have been deleted in the file, while
            # taking into account that the db may have tags not
            # supported by the file's tag format.
            if f.others:
                supported_tags = [t for t in self.list_tags()
                                  if not t.startswith("__")]
            else:
                supported_tags = f.tag_mapping.keys()
            for tag in supported_tags:
                if tag not in ntags.keys():
                    self.set_tag_raw(tag, None)

            # fill out file specific items
            mtime = unicode(datetime.fromtimestamp(os.stat(self.get_loc()).st_mtime).strftime(datetime_format))
            self.set_tag_raw('__modified', mtime)
            # TODO: this probably breaks on non-local files
            self.set_tag_raw('__basedir', self.get_basedir())
            self.set_tag_raw('__basename', self.get_basename())
            self._scan_valid = True
            return f
        except Exception, e:
            print e
            self._scan_valid = False
            return False

    def write_tags(self):
        """
            Writes tags to the file for this Track.

            Returns False if unsuccessful, and a Format object from
            `xl.metadata` otherwise.
        """
        try:
            f = metadata.get_format(self.get_loc())
            if f is None:
                return False  # not a supported type
            f.write_tags(self.__tags)
            return f
        except IOError:
            return False
        except Exception:
            return False

    def read_tags(self):
        """
            Reads tags from the file for this Track.

            Returns False if unsuccessful, and a Format object from
            `xl.metadata` otherwise.
        """
        try:
            f = metadata.get_format(self.get_loc())
            if f is None:
                self._scan_valid = False
                return False # not a supported type
            ntags = f.read_all()
            for k, v in ntags.iteritems():
                self.__tags[k] = v

            # remove tags that have been deleted in the file, while
            # taking into account that the db may have tags not
            # supported by the file's tag format.
            if f.others:
                supported_tags = [ t for t in self.list_tags() \
                        if not t.startswith("__") ]
            else:
                supported_tags = f.tag_mapping.keys()
            for tag in supported_tags:
                if tag not in ntags.keys():
                    self.__tags[tag] = None

            # fill out file specific items
            mtime = time.ctime(os.path.getmtime(self.get_loc()))
            self.__tags['__modified'] = mtime
            # TODO: this probably breaks on non-local files
            path = os.path.dirname(self.get_loc())
            self.__tags['__basedir'] = path
            self._scan_valid = True
            return f
        except Exception:
            self._scan_valid = False
            return False