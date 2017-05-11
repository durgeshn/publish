class Agent(object):
    def __init__(self, name):
        self.name = name


class AgentX(object):
    def __init__(self, name1):
        self.name1 = name1


class MyAgent(Agent, AgentX):
    def __init__(self, name, name1):
        super(MyAgent, self).__init__(name)
        # super(MyAgentX, self).__init__(name1)
        AgentX.__init__(self, name1)
        print 'AAA'


if __name__ == '__main__':
    d = MyAgent('durgesh', 'amol')
    print d.name
    print d.name1
