# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_compare/cmp_cart_popover.py
from debug_utils import LOG_ERROR
from gui.Scaleform import getNationsFilterAssetPath
from gui.Scaleform.daapi.view.lobby.vehicle_compare.formatters import packHeaderColumnData
from gui.Scaleform.daapi.view.meta.VehicleCompareCartPopoverMeta import VehicleCompareCartPopoverMeta
from gui.Scaleform.framework.entities.DAAPIDataProvider import SortableDAAPIDataProvider
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.locale.VEH_COMPARE import VEH_COMPARE
from gui.game_control import getVehicleComparisonBasketCtrl
from gui.prb_control.dispatcher import g_prbLoader
from gui.shared.ItemsCache import g_itemsCache
from gui.shared.event_dispatcher import showVehicleCompare
from gui.shared.formatters import text_styles
from helpers.i18n import makeString as _ms
from nations import AVAILABLE_NAMES

class VehicleCompareCartPopover(VehicleCompareCartPopoverMeta):

    def __init__(self, ctx = None):
        super(VehicleCompareCartPopover, self).__init__(ctx)

    def remove(self, vehId):
        getVehicleComparisonBasketCtrl().removeVehicleByIdx(int(vehId))

    def removeAll(self):
        getVehicleComparisonBasketCtrl().removeAllVehicles()

    def _onRegisterFlashComponent(self, viewPy, alias):
        super(VehicleCompareCartPopover, self)._onRegisterFlashComponent(viewPy, alias)

    def onWindowClose(self):
        self.destroy()

    def gotoCompareView(self):
        showVehicleCompare()
        self.destroy()

    def _populate(self):
        super(VehicleCompareCartPopover, self)._populate()
        self._cartDP = _VehicleCompareCartDataProvider()
        self._cartDP.setFlashObject(self.as_getDPS())
        comparisonBasket = getVehicleComparisonBasketCtrl()
        self._cartDP.rebuildList(comparisonBasket.getVehiclesCDs())
        comparisonBasket.onChange += self.__onBasketChange
        comparisonBasket.onSwitchChange += self.onWindowClose
        self.__initControls()

    def _dispose(self):
        super(VehicleCompareCartPopover, self)._dispose()
        comparisonBasket = getVehicleComparisonBasketCtrl()
        comparisonBasket.onChange -= self.__onBasketChange
        comparisonBasket.onSwitchChange -= self.onWindowClose
        self._cartDP.fini()
        self._cartDP = None
        return

    def __initControls(self):
        headers = [packHeaderColumnData('nationId', 49, 30, tooltip=VEH_COMPARE.CARTPOPOVER_SORTING_NATION, icon=RES_ICONS.MAPS_ICONS_FILTERS_NATIONS_ALL),
         packHeaderColumnData('typeIndex', 45, 30, tooltip=VEH_COMPARE.CARTPOPOVER_SORTING_VEHTYPE, icon=RES_ICONS.MAPS_ICONS_FILTERS_TANKS_ALL),
         packHeaderColumnData('level', 45, 30, tooltip=VEH_COMPARE.CARTPOPOVER_SORTING_VEHLVL, icon=RES_ICONS.MAPS_ICONS_BUTTONS_TAB_SORT_BUTTON_LEVEL),
         packHeaderColumnData('shortUserName', 140, 30, label=VEH_COMPARE.CARTPOPOVER_SORTING_VEHNAME, tooltip=VEH_COMPARE.CARTPOPOVER_SORTING_VEHNAME_TOOLTIP),
         packHeaderColumnData('actions', 1, 30)]
        self.as_setInitDataS({'title': text_styles.highTitle(_ms(VEH_COMPARE.CARTPOPOVER_TITLE)),
         'tableHeaders': headers})
        self.__updateButtonsState()

    def __onBasketChange(self, _):
        self.__updateButtonsState()

    def __updateButtonsState(self):
        basket = getVehicleComparisonBasketCtrl()
        count = basket.getVehiclesCount()
        buttonsEnabled = count > 0
        if basket.isFull():
            addBtnTT = VEH_COMPARE.CARTPOPOVER_FULLBASKETCMPBTN_TOOLTIP
            addBtnIcon = RES_ICONS.MAPS_ICONS_BUTTONS_ALERTICON
        else:
            addBtnTT = VEH_COMPARE.CARTPOPOVER_OPENCMPBTN_TOOLTIP
            addBtnIcon = None
        isNavigationEnabled = not g_prbLoader.getDispatcher().getFunctionalState().isNavigationDisabled()
        self.as_updateToCmpBtnPropsS({'btnLabel': _ms(VEH_COMPARE.CARTPOPOVER_GOTOCOMPAREBTN_LABEL, value=count),
         'btnTooltip': addBtnTT,
         'btnEnabled': buttonsEnabled and isNavigationEnabled,
         'btnIcon': addBtnIcon})
        self.as_updateClearBtnPropsS({'btnLabel': VEH_COMPARE.CARTPOPOVER_REMOVEALLBTN_LABEL,
         'btnTooltip': VEH_COMPARE.CARTPOPOVER_REMOVEALLBTN_TOOLTIP,
         'btnEnabled': buttonsEnabled})
        return


class _VehicleCompareCartDataProvider(SortableDAAPIDataProvider):

    def __init__(self):
        super(_VehicleCompareCartDataProvider, self).__init__()
        self._list = []
        self._listMapping = {}
        self.__mapping = {}
        self.__selectedID = None
        return

    @property
    def collection(self):
        return self._list

    def emptyItem(self):
        return None

    def clear(self):
        self._list = []
        self._listMapping.clear()
        self.__mapping.clear()
        self.__selectedID = None
        return

    def fini(self):
        getVehicleComparisonBasketCtrl().onChange -= self.__onComparisonVehsChanged
        self.clear()
        self._dispose()

    def getSelectedIdx(self):
        if self.__selectedID in self.__mapping:
            return self.__mapping[self.__selectedID]
        return -1

    def setSelectedID(self, selId):
        self.__selectedID = selId

    def setFlashObject(self, movieClip, autoPopulate = True, setScript = True):
        getVehicleComparisonBasketCtrl().onChange += self.__onComparisonVehsChanged
        return super(_VehicleCompareCartDataProvider, self).setFlashObject(movieClip, autoPopulate, setScript)

    def getVO(self, index):
        vo = None
        if index > -1:
            try:
                vo = self.sortedCollection[index]
            except IndexError:
                LOG_ERROR('Item not found', index)

        return vo

    def buildList(self, changedVehsCDs):
        self.clear()
        for idx, vehCD in enumerate(changedVehsCDs):
            self._list.append(self._makeVO(vehCD, idx))

    def rebuildList(self, cache):
        self.buildList(cache)
        self.refresh()

    def pyGetSelectedIdx(self):
        return self.getSelectedIdx()

    def refreshRandomItems(self, indexes, items):
        self.flashObject.invalidateItems(indexes, items)

    def refreshSingleItem(self, index, item):
        self.flashObject.invalidateItem(index, item)

    def _makeVO(self, vehicleCD, index):
        vehicle = g_itemsCache.items.getItemByCD(vehicleCD)
        if vehicle.isPremium:
            moduleType = 'premium'
        else:
            moduleType = getVehicleComparisonBasketCtrl().getVehicleAt(index).getModulesType()
        complectation = _ms(VEH_COMPARE.cartpopover_moduletype(moduleType))
        return {'id': vehicleCD,
         'index': index,
         'vehicleName': text_styles.main(vehicle.shortUserName),
         'complectation': complectation,
         'nation': getNationsFilterAssetPath(AVAILABLE_NAMES[vehicle.nationID]),
         'level': vehicle.level,
         'typeStr': vehicle.type,
         'smallIconPath': vehicle.iconSmall,
         'removeBtnTooltip': VEH_COMPARE.CARTPOPOVER_REMOVEBTN_TOOLTIP}

    def __onComparisonVehsChanged(self, changedData):
        """
        gui.game_control.VehComparisonBasket.onChange event handler
        :param changedData: instance of gui.game_control.veh_comparison_basket._ChangedData
        """
        self.rebuildList(getVehicleComparisonBasketCtrl().getVehiclesCDs())