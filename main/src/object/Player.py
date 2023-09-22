"""sumary_line

Keyword arguments:
argument -- description
Return: return_description

TODO: Update Docstrings

"""
from abc import ABC, abstractmethod
from typing import Tuple
from enum import EnumType
from ..Object import Object  # pylint: disable = import-error, no-name-in-module
from .PlayerWeapon import PlayerWeapon
from .PlayerEnemy import ( # pylint: disable = import-error, no-name-in-module
    PlayerEnemy, # pylint: disable = import-error, no-name-in-module
)  # pylint: disable = import-error, no-name-in-module


class Player(Object, PlayerWeapon, PlayerEnemy, ABC):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def __init__(self):
        Object.__init__(self)  # pylint: disable = W,E
        self.elements: Tuple[
            Tuple[object]
        ] = self.init_elements()  # pylint: disable = W,E
        self.states: Tuple[
            Tuple[EnumType]
        ] = self.init_states()  # pylint: disable = W,E

    @abstractmethod
    def run(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    @abstractmethod
    def notify_states(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    @abstractmethod
    def init_elements(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    @abstractmethod
    def init_states(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    @abstractmethod
    def death(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    @abstractmethod
    def take_hit(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    @abstractmethod
    def move(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    @abstractmethod
    def fire(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    @abstractmethod
    def reload(self):
        """sumary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError

    @abstractmethod
    def apply_effects(self):
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        raise NotImplementedError
