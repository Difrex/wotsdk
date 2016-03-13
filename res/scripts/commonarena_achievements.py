# Embedded file name: scripts/common/arena_achievements.py
from dossiers2.custom.records import RECORD_DB_IDS
ACHIEVEMENTS = ('warrior', 'invader', 'sniper', 'sniper2', 'mainGun', 'defender', 'steelwall', 'supporter', 'scout', 'evileye', 'medalWittmann', 'medalOrlik', 'medalOskin', 'medalHalonen', 'medalBurda', 'medalBillotte', 'medalKolobanov', 'medalFadin', 'medalRadleyWalters', 'medalLafayettePool', 'medalLehvaslaiho', 'medalNikolas', 'medalPascucci', 'medalDumitru', 'medalBrunoPietro', 'medalTarczay', 'heroesOfRassenay', 'medalDeLanglade', 'medalTamadaYoshio', 'raider', 'kamikaze', 'huntsman', 'bombardier', 'luckyDevil', 'ironMan', 'sturdy', 'alaric', 'lumberjack', 'medalBrothersInArms', 'medalCrucialContribution', 'armoredFist', 'kingOfTheHill', 'willToWinSpirit', 'shoulderToShoulder', 'aloneInTheField', 'fallenFlags', 'effectiveSupport', 'falloutDieHard', 'stormLord', 'winnerLaurels', 'predator', 'unreachable', 'champion', 'bannerman', 'sauronEye')
ACHIEVEMENTS_WITH_REWARD = set([ RECORD_DB_IDS['achievements', name] for name in ('warrior', 'invader', 'sniper', 'sniper2', 'mainGun', 'defender', 'steelwall', 'supporter', 'scout', 'evileye', 'heroesOfRassenay', 'medalFadin', 'medalNikolas', 'medalPascucci', 'medalLehvaslaiho', 'medalRadleyWalters', 'medalHalonen', 'medalDumitru', 'medalDeLanglade', 'medalOrlik', 'medalOskin', 'medalLafayettePool', 'medalBurda', 'medalTamadaYoshio', 'medalBrothersInArms', 'medalCrucialContribution', 'huntsman', 'medalStark', 'medalGore') ] + [ RECORD_DB_IDS['falloutAchievements', name] for name in ('shoulderToShoulder', 'falloutDieHard', 'champion', 'bannerman') ])
INBATTLE_SERIES = ('sniper', 'killing', 'piercing')
INBATTLE_SERIES_INDICES = dict(((x[1], x[0]) for x in enumerate(INBATTLE_SERIES)))
_BILLOTTE_CMN_CNDS = {'hpPercentage': 20,
 'minCrits': 5}
ACHIEVEMENT_CONDITIONS = {'warrior': {'minFrags': 6},
 'invader': {'minCapturePts': 80},
 'sniper': {'minAccuracy': 0.85,
            'minShots': 10,
            'minDamage': 1000},
 'sniper2': {'minAccuracy': 0.85,
             'minDamage': 1000,
             'minHitsWithDamagePercent': 0.8,
             'sniperDistance': 300.0,
             'minShots': 8},
 'mainGun': {'minDamage': 1000,
             'minDamageToTotalHealthRatio': 0.2},
 'defender': {'minPoints': 70},
 'steelwall': {'minDamage': 1000,
               'minHits': 11},
 'supporter': {'minAssists': 6},
 'scout': {'minDetections': 9},
 'evileye': {'minAssists': 6},
 'medalRadleyWalters': {'minLevel': 5,
                        'minKills': 8,
                        'maxKills': 9},
 'medalLafayettePool': {'minLevel': 5,
                        'minKills': 10,
                        'maxKills': 13},
 'heroesOfRassenay': {'minKills': 14,
                      'maxKills': 255},
 'medalOrlik': {'minVictimLevelDelta': 2,
                'minKills': 3},
 'medalLehvaslaiho': {'minVictimLevelDelta': 2,
                      'minKills': 2,
                      'maxKills': 2},
 'medalOskin': {'minVictimLevelDelta': 2,
                'minKills': 3,
                'maxKills': 3},
 'medalNikolas': {'minVictimLevelDelta': 2,
                  'minKills': 4,
                  'maxKills': 255},
 'medalHalonen': {'minVictimLevelDelta': 2,
                  'minKills': 3},
 'medalPascucci': {'minKills': 3,
                   'maxKills': 3},
 'medalDumitru': {'minKills': 4,
                  'maxKills': 4},
 'medalBurda': {'minKills': 5,
                'maxKills': 255},
 'medalBillotte': {'cmn_cnds': _BILLOTTE_CMN_CNDS,
                   'minKills': 2,
                   'maxKills': 2},
 'medalBrunoPietro': {'cmn_cnds': _BILLOTTE_CMN_CNDS,
                      'minKills': 3,
                      'maxKills': 4},
 'medalTarczay': {'cmn_cnds': _BILLOTTE_CMN_CNDS,
                  'minKills': 5,
                  'maxKills': 255},
 'medalKolobanov': {'teamDiff': 5},
 'medalBrothersInArms': {'minKills': 3},
 'medalCrucialContribution': {'minKills': 12},
 'medalDeLanglade': {'minKills': 4},
 'medalTamadaYoshio': {'minKills': 3,
                       'maxKills': 255,
                       'minVictimLevelDelta': 2},
 'kamikaze': {'levelDelta': 1},
 'huntsman': {'minKills': 3},
 'bombardier': {'minKills': 2},
 'luckyDevil': {'radius': 10.99},
 'ironMan': {'minHits': 10},
 'sturdy': {'minHealth': 10.0},
 'alaric': {'minKills': 2,
            'minMonuments': 1},
 'lumberjack': {'minKills': 3,
                'minTrees': 30},
 'wolfAmongSheep': {'minDamage': 1},
 'geniusForWar': {'minXP': 1},
 'willToWinSpirit': {'enemyCount': 3},
 'fightingReconnaissance': {'maxPosInTopDamager': 3,
                            'minSpottedCount': 2},
 'monolith': {'maxSpeed_ms': 11 / 3.6},
 'medalAntiSpgFire': {'minKills': 3},
 'medalStark': {'minKills': 2,
                'hits': 2},
 'medalGore': {'minDamageRate': 10},
 'medalCoolBlood': {'maxDistance': 100,
                    'minKills': 2},
 'promisingFighter': {'maxPosInTopXPGainer': 3},
 'heavyFire': {'maxPosInTopDamager': 3},
 'fighter': {'minKills': 4,
             'maxKills': 5},
 'duelist': {'minKills': 2},
 'bonecrusher': {'minCrits': 5},
 'charmed': {'minVehs': 4},
 'tacticalAdvantage': {'maxLevel': 7},
 'secretOperations': {'minGroupLen': 2},
 'shoulderToShoulder': {'minKills': 12,
                        'minDamageDealt': 30000},
 'aloneInTheField': {'minDamageDealt': 10000},
 'fallenFlags': {'minFlags': 4},
 'effectiveSupport': {'minDamageDealt': 2000},
 'falloutDieHard': {'minKills': 5,
                    'minDamageDealt': 10000},
 'predator': {'minKills': 5},
 'champion': {'minKills': 5,
              'minDamageDealt': 10000,
              'minFlagsCapture': 3},
 'bannerman': {'minFlagsCapture': 4}}