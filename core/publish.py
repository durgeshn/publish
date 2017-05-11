"""
This is the module responsible for the publish process.
"""
import os

#
import sys
sys.path.insert(0, r'\\stor\Data\python_packages\repo\pathGenerator\v001')

from path_generator import ProjectpathGenerator


class Publish(object):
    def __init__(self, project):
        super(Publish, self).__init__()
        self.proj = project
        self.path_dict = dict()
        self.path_gen = None
        # self.doValidations()

    @property
    def getConfigFile(self):
        rootFolder = os.path.dirname(__file__)
        configFolder = rootFolder.replace('/core', '/config')
        configFile = os.path.join(configFolder, '%s_config.txt' % self.proj.lower()).replace('\\', '/')
        if not os.path.isfile(configFile):
            configFile = os.path.join(configFolder, 'default').replace('\\', '/')
        return configFile

    # break down the path provided to the bases.
    def path_break(self, path_to_brk):
        print self.proj
        return path_to_brk

    def read_config(self, head):
        file_read = open(self.getConfigFile, 'r')
        ret = {}
        start = 0
        for each_line in file_read.readlines():
            each_line = each_line.strip()
            # print each_line
            if not each_line:
                start = 0
            if start and each_line:
                tmp = each_line.split('=')
                ret[tmp[0].strip()] = tmp[1].strip()
            if each_line.startswith(head):
                start = 1
        # print "ret#########",ret
        return ret

    # get all kind of paths here in a single dict.
    def getAllPaths(self):
        return self.read_config('[PATH]')

    # Validations.
    def doValidations(self):
        pass

    # pre hooks for the publish process.
    def doPreHooks(self):
        pass

    # Publish.
    def doPublish(self):
        pass

    # post hooks for the publish process.
    def doPostHooks(self):
        pass

    # do the process here.
    def run(self):
        self.doPreHooks()
        self.doPublish()
        self.doPostHooks()
        self.doDataEntry()

    # data base entry.
    def doDataEntry(self):
        pass


if __name__ == '__main__':
    pub = Publish('MTB')
    # print pub.path_break(r"P:\badgers_and_foxes\01_SAISON_1\13_PRODUCTION\04_EPISODES\02_Fabrication_3D\BDG102\
    # sh002\lay\maya\work\BDG102_002_lay_005.ma")
    print pub.getAllPaths()
