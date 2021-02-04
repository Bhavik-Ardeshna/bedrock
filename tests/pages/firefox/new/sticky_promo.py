# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected

from pages.base import BasePage
from pages.regions.sticky_promo import StickyPromo


class StickyPromoPage(BasePage):

    URL_TEMPLATE = '/{locale}/firefox/new/'

    # Used as a scroll target to move down the page, to trigger the sticky promo element
    _page_highlights_content_locator = (By.CSS_SELECTOR, '.t-highlights')
    _sticky_promo_modal_content_locator = (By.CSS_SELECTOR, '.mzp-c-sticky-promo.mzp-a-slide-in')

    def init_promo(self):
        assert not self.is_promo_displayed, 'Promo detail is not displayed'
        # scroll down page to trigger promo to display
        self.scroll_element_into_view(*self._page_highlights_content_locator)
        self.wait.until(expected.visibility_of_element_located(
            self._sticky_promo_modal_content_locator))

    @property
    def is_promo_displayed(self):
        return self.is_element_displayed(*self._sticky_promo_modal_content_locator)

    @property
    def promo(self):
        return StickyPromo(self)
