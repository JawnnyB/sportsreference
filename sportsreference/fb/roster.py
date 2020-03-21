from .constants import SQUAD_URL


class SquadPlayer:
    def __init__(self, player_data):
        self._name = None
        self._player_id = None
        self._nationality = None
        self._position = None
        self._age = None
        self._matches_played = None
        self._starts = None
        self._minutes = None
        self._goals = None
        self._assists = None
        self._penalty_kicks = None
        self._penalty_kick_attempts = None
        self._yellow_cards = None
        self._red_cards = None
        self._goals_per_90 = None
        self._assists_per_90 = None
        self._goals_and_assists_per_90 = None
        self._goals_non_penalty_per_90 = None
        self._goals_and_assists_non_penalty_per_90 = None
        self._expected_goals = None
        self._expected_goals_non_penalty = None
        self._expected_assists = None
        self._expected_goals_per_90 = None
        self._expected_assists_per_90 = None
        self._expected_goals_and_assists_per_90 = None
        self._expected_goals_non_penalty_per_90 = None
        self._expected_goals_and_assists_non_penalty_per_90 = None
        self._own_goals = None
        # Goalkeeping stats
        self._goals_against = None
        self._goals_against_per_90 = None
        self._shots_on_target_against = None
        self._saves = None
        self._save_percentage = None
        self._wins = None
        self._draws = None
        self._losses = None
        self._clean_sheets = None
        self._clean_sheet_percentage = None
        self._penalty_kicks_attempted = None
        self._penalty_kicks_allowed = None
        self._penalty_kicks_saved = None
        self._penalty_kicks_missed = None
        # Advanced goalkeeping stats
        self._free_kick_goals_against = None
        self._corner_kick_goals_against = None
        self._post_shot_expected_goals = None
        self._post_shot_expected_goals_per_sot = None
        self._post_shot_expected_goals_minus_allows = None
        self._launches_completed = None
        self._launches_attempted = None
        self._launch_completion_percentage = None
        self._keeper_passes_attempted = None
        self._throws_attempted = None
        self._launch_percentage = None
        self._average_keeper_pass_length = None
        self._goal_kicks_attempted = None
        self._goal_kick_launch_percentage = None
        self._average_goal_kick_length = None
        self._opponent_cross_attempts = None
        self._opponent_cross_stops = None
        self._opponent_cross_stop_percentage = None
        self._keeper_actions_outside_penalty_area = None
        self._keeper_actions_outside_penalty_area_per_90 = None
        self._average_keeper_action_outside_penalty_distance = None
        # Shooting stats
        self._nineties_played = None
        self._shots = None
        self._shots_on_target = None
        self._free_kick_shots = None
        self._shots_on_target_percentage = None
        self._shots_per_90 = None
        self._shots_on_target_per_90 = None
        self._goals_per_shot = None
        self._goals_per_shot_on_target = None
        self._expected_goals_non_penalty_per_shot = None
        self._goals_minus_expected = None
        self._non_penalty_minus_expected_non_penalty = None
        # Passing stats
        self._assists_minus_expected = None
        self._key_passes = None
        self._passes_completed = None
        self._passes_attempted = None
        self._pass_completion = None
        self._short_passes_completed = None
        self._short_passes_attempted = None
        self._short_pass_completion = None
        self._medium_passes_completed = None
        self._medium_passes_attempted = None
        self._medium_pass_completion = None
        self._long_passes_completed = None
        self._long_passes_attempted = None
        self._long_pass_completion = None
        self._left_foot_passes = None
        self._right_foot_passes = None
        self._free_kick_passes = None
        self._through_balls = None
        self._corner_kicks = None
        self._throw_ins = None
        self._final_third_passes = None
        self._penalty_area_passes = None
        self._penalty_area_crosses = None
        # Playing time stats


class Roster:
    def __init__(self, squad_id):
        self._players = []

    def _pull_stats(self):
        doc = pq(SQUAD_URL % self.squad_id)
        standard_table = 'table#stats_standard_ks_combined tbody'
        stats = utils._get_stats_table(doc, standard_table)
        goalkeeping_table = 'table#stats_keeper_ks_combined_clone tbody'
        goalkeeping = utils._get_stats_table(doc, goalkeeping_table)
        advanced_keepers = 'table#stats_keeper_adv_ks_combined_clone tbody'
        advanced_keepers = utils._get_stats_table(doc, advanced_keepers)
        shooting_table = 'table#stats_shooting_ks_combined_clone tbody'
        shooting = utils._get_stats_table(doc, shooting_table)
        passing_table = 'table#stats_passing_ks_combined_clone tbody'
        passing = utils._get_stats_table(doc, passing_table)
        time_table = 'table#stats_playing_time_ks_combined_clone tbody'
        time = utils._get_stats_table(doc, time_table)
        miscellaneous = 'table#stats_misc_ks_combined_clone tbody'
        miscellaneous = utils._get_stats_table(doc, miscellaneous)
        player_summary = 'table#stats_player_summary_clone tbody'
        player_summary = utils._get_stats_table(doc, player_summary)
        keeper_summary = 'table#stats_keeper_summary_clone tbody'
        keeper_summary = utils._get_stats_table(doc, keeper_summary)
