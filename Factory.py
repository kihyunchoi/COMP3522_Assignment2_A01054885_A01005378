import abc
from Candy import CandyCanes, PumpkinCaramelToffee, CremeEggs
from Toy import SantasWorkshop, RCSpider, RobotBunny
from StuffedAnimal import EasterBunny, DancingSkeleton, Reindeer


class Factory(abc.ABC):
    """
    A factory that creates shop items.
    """

    @abc.abstractmethod
    def create_candy(self, name, product_id, **kwargs):
        pass

    @abc.abstractmethod
    def create_toy(self, name, product_id, **kwargs):
        pass

    @abc.abstractmethod
    def create_stuffed_animal(self, name, product_id, **kwargs):
        pass


class ChristmasFactory(Factory):
    """
    A factory that creates Christmas items.
    """

    def create_candy(self, name, product_id, **kwargs):
        """
        Create Candy Cane item.
        :param product_id: String
        :param name: String
        :param kwargs: dictionary
        :return: CandyCane
        """
        return CandyCanes(name, product_id, **kwargs)

    def create_toy(self, name, product_id, **kwargs):
        """
        Create a Santa's Workshop item.
        :param product_id: String
        :param name: String
        :param kwargs: dictionary
        :return: SantasWorkshop
        """
        return SantasWorkshop(name, product_id, **kwargs)

    def create_stuffed_animal(self, name, product_id, **kwargs):
        """
        Create a Reindeer item.
        :param product_id: String
        :param name: String
        :param kwargs: dictionary
        :return: Reindeer
        """
        return Reindeer(name, product_id, **kwargs)


class HalloweenFactory(Factory):
    """
    A factory that creates Halloween items.
    """
    def create_candy(self, name, product_id, **kwargs):
        """
        Create a Pumpking Caramel Toffee.
        :param product_id: String
        :param name: String
        :param kwargs: dictionary
        :return: PumpkinCaramelToffee
        """
        return PumpkinCaramelToffee(name, product_id, **kwargs)

    def create_toy(self, name, product_id, **kwargs):
        """
        Create an RC Spider toy.
        :param product_id: String
        :param name: String
        :param kwargs: dictionary
        :return: RCSpider
        """
        return RCSpider(name, product_id, **kwargs)

    def create_stuffed_animal(self, name, product_id, **kwargs):
        """
        Create a Dancing Skeleton.
        :param product_id: String
        :param name: String
        :param kwargs: dictionary
        :return: DancingSkeleton
        """
        return DancingSkeleton(name, product_id, **kwargs)


class EasterFactory(Factory):
    """
    A factory that creates Easter items.
    """
    def create_candy(self, name, product_id, **kwargs):
        """
        Create Creme Eggs.
        :param product_id: String
        :param name: String
        :param kwargs: dictionary
        :return: CremeEggs
        """
        return CremeEggs(name, product_id, **kwargs)

    def create_toy(self, name, product_id, **kwargs):
        """
        Create a Robot Bunny.
        :param product_id: String
        :param name: String
        :param kwargs: dictionary
        :return: RobotBunny
        """
        return RobotBunny(name, product_id, **kwargs)

    def create_stuffed_animal(self, name, product_id, **kwargs):
        """
        Create an Easter Bunny.
        :param product_id: String
        :param name: String
        :param kwargs: dictionary
        :return: EasterBunny
        """
        return EasterBunny(name, product_id, **kwargs)
