# PlayersStats/Normal/winger.py

from ..player import Player

class Winger(Player):
    def __init__(self):
        super().__init__('Winger')

    def get_stat_config(self):
        stat_config = super().get_stat_config()

        # Winger-specific adjustments
        stat_config['Mental']['Composure'] = {'mean': 55, 'std_dev': 6}
        stat_config['Athletic']['Physical Power']['mean'] = 50
        stat_config['Athletic']['Ball Control']['mean'] = 65
        stat_config['Athletic']['Dribbling']['mean'] = 70
        stat_config['Athletic']['Jumping']['mean'] = 55
        stat_config['Athletic']['Acceleration']['mean'] = 70
        stat_config['Athletic']['Speed'] = {'mean': 70, 'std_dev': 8}

        # Defense stats
        stat_config['Defense'] = {
            'Tackling': {'mean': 30, 'std_dev': 4},
            'Marking': {'mean': 30, 'std_dev': 4},
            'Positioning': {'mean': 50, 'std_dev': 4},
        }

        # Attack stats
        stat_config['Attack'] = {
            'Finishing': {'mean': 65, 'std_dev': 4},
            'Long Shots': {'mean': 65, 'std_dev': 4},
            'Off The Ball': {'mean': 70, 'std_dev': 4},
        }

        # Playmaking
        stat_config['Playmaking']['Crossing'] = {'mean': 70, 'std_dev': 4}

        return stat_config