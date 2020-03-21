import abc
from Candy import CandyCanes, PumpkinCaramelToffee, CremeEggs
from Toy import SantasWorkshop, RCSpider, RobotBunny
from StuffedAnimal import EasterBunny, DancingSkeleton, Reindeer


class Factory(abc.ABC):
    """
    A factory that creates shop items.
    """

    @abc.abstractmethod
    def create_candy(self, **kwargs):
        pass

    @abc.abstractmethod
    def create_toy(self, **kwargs):
        pass

    @abc.abstractmethod
    def create_stuffed_animal(self, **kwargs):
        pass


class ChristmasFactory(Factory):
    """
    A factory that creates Christmas items.
    """

    def create_candy(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        return CandyCanes(**kwargs)

    def create_toy(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        return SantasWorkshop(**kwargs)

    def create_stuffed_animal(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        return Reindeer(**kwargs)


class HalloweenFactory(Factory):
    """
    A factory that creates Halloween items.
    """
    def create_candy(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        return PumpkinCaramelToffee(**kwargs)

    def create_toy(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        return RCSpider(**kwargs)

    def create_stuffed_animal(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        return DancingSkeleton(**kwargs)


class EasterFactory(Factory):
    """
    A factory that creates Easter items.
    """
    def create_candy(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        return CremeEggs(**kwargs)

    def create_toy(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        return RobotBunny(**kwargs)

    def create_stuffed_animal(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        return EasterBunny(**kwargs)