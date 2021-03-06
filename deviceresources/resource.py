#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod, abstractproperty
from threading import RLock


class Resource:
    "Абстрактный класс ресурсов"
    __metaclass__ = ABCMeta

    NUM_LEDS = 32
    DEFAULT_VALUE = [0x0, 0x0, 0x0]

    def __init__(self):
        self.lock = RLock()

    @abstractmethod
    def setResource(self, resource): pass

    @abstractmethod
    def getResource(self): pass

    @abstractmethod
    def changed(self):
        """ Абстрактный метод определения изменилось ли что-нибуь в данных
        или нет"""
        pass

    @abstractmethod
    def save(self): pass

    def equal(self, old, new):
        """Проверка равенства двух массивов"""
        if all(map(lambda a, b: a == b, old, new)):
            return True
        else:
            return False

    def set(self, resource):
        # захватываем блокировку
        with self.lock:
            self.setResource(resource)

    def get(self):
        with self.lock:
            resource = self.getResource()

        return resource

    def getBlock(self):
        return self.lock

    def block(self):
        self.lock.acquire()

    def unblock(self):
        self.lock.release()
