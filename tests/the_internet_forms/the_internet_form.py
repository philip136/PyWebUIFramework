from abc import ABC, abstractmethod

from forms.base_form import BaseForm
from tests.constants import UrlConstants


class TheInternetForm(ABC, BaseForm):
    __the_internet_form_url = UrlConstants.THE_INTERNET

    @property
    def url(self):
        return self.__the_internet_form_url + self._uri

    @property
    @abstractmethod
    def uri(self):
        pass
