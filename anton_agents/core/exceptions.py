"""异常体系"""


class AntonAgentsException(Exception):
    """AntonAgents基础异常类"""

    pass


class LLMException(AntonAgentsException):
    """LLM相关异常"""

    pass


class AgentException(AntonAgentsException):
    """Agent相关异常"""

    pass


class ConfigException(AntonAgentsException):
    """配置相关异常"""

    pass


class ToolException(AntonAgentsException):
    """工具相关异常"""

    pass
