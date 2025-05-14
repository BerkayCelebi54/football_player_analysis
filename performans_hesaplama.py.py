def calculate_player_technical_performance(player_data, max_shots, max_tackles, max_passes):
    scores = {}

    for player in player_data:
        scores[player['name']] = {}

        # Long Shot Calculation
        long_shots = player['long_shots']
        goals = player['goals']
        accurate_shots = player['accurate_shots']
        xg = player['xg']
        
        long_shot_score = (
            (goals / long_shots) * 100 * 0.40 +
            (accurate_shots / long_shots) * 100 * 0.25 +
            ((goals - xg) / xg) * 100 * 0.25 +
            (long_shots / max_shots) * 100 * 0.15
        )

        # Penalty Calculation
        penalty_shots = player['penalty_shots']
        penalty_goals = player['penalty_goals']
        penalty_accurate = player['penalty_accurate']
        penalty_xg = player['penalty_xg']
        
        penalty_score = (
            (penalty_goals / penalty_shots) * 100 * 0.40 +
            (penalty_accurate / penalty_shots) * 100 * 0.25 +
            ((penalty_goals - penalty_xg) / penalty_xg) * 100 * 0.25 +
            (penalty_shots / max_shots) * 100 * 0.15
        )

        # Free Kick Calculation
        fk_shots = player['free_kick_shots']
        fk_goals = player['free_kick_goals']
        fk_accurate = player['free_kick_accurate']
        fk_xg = player['free_kick_xg']
        
        free_kick_score = (
            (fk_goals / fk_shots) * 100 * 0.40 +
            (fk_accurate / fk_shots) * 100 * 0.25 +
            ((fk_goals - fk_xg) / fk_xg) * 100 * 0.25 +
            (fk_shots / max_shots) * 100 * 0.15
        )

        # Finishing Calculation
        box_shots = player['box_shots']
        box_goals = player['box_goals']
        box_accurate = player['box_accurate']
        box_xg = player['box_xg']
        
        finishing_score = (
            (box_goals / box_shots) * 100 * 0.40 +
            (box_accurate / box_shots) * 100 * 0.25 +
            ((box_goals - box_xg) / box_xg) * 100 * 0.25 +
            (box_shots / max_shots) * 100 * 0.15
        )

        # Crossing Skill
        crosses = player['crosses']
        cross_success = player['cross_success']
        
        crossing_score = (
            (cross_success / crosses) * 100 * 0.50 +
            (crosses / max_shots) * 100 * 0.50
        )

        # First Touch
        first_touch_score = (
            (player['first_touch_success'] / player['first_touch_attempts']) * 100 * 0.60 +
            (player['first_touch_volume'] / max_shots) * 100 * 0.40
        )

        # Throw-in
        throw_success = player['throw_success']
        throw_count = player['throw_count']
        
        throw_score = (
            (throw_success / throw_count) * 100 * 0.50 +
            (throw_count / max_shots) * 100 * 0.50
        )

        # Heading
        header_success = player['header_success']
        header_count = player['header_count']
        
        header_score = (
            (header_success / header_count) * 100 * 0.60 +
            (header_count / max_shots) * 100 * 0.40
        )

        # Marking
        marking_success = player['marking_success']
        marking_attempts = player['marking_attempts']
        
        marking_score = (
            (marking_success / marking_attempts) * 100 * 0.50 +
            (marking_attempts / max_shots) * 100 * 0.50
        )

        # Tackling
        total_tackles = player['total_tackles']
        ball_recovery = player['ball_recovery']
        opponent_tackles = player['opponent_tackles']
        
        recovery_rate = (ball_recovery / opponent_tackles) * 100 if opponent_tackles > 0 else 0
        tackle_success_rate = (ball_recovery / total_tackles) * 100 if total_tackles > 0 else 0
        tackle_performance = tackle_success_rate
        tackle_volume = (ball_recovery / max_tackles) * 100 if max_tackles > 0 else 0
        
        tackle_score = (
            recovery_rate * 0.40 +
            tackle_success_rate * 0.30 +
            tackle_performance * 0.20 +
            tackle_volume * 0.10
        )

        # Passing
        total_passes = player['total_passes']
        accurate_passes = player['accurate_passes']
        assists = player['assists']
        
        pass_accuracy = (accurate_passes / total_passes) * 100 if total_passes > 0 else 0
        pass_volume = (total_passes / max_passes) * 100 if max_passes > 0 else 0
        
        pass_score = (
            pass_accuracy * 0.40 +
            pass_volume * 0.30 +
            assists * 0.30
        )

        # Final Score Record
        scores[player['name']] = {
            'long_shot_score': long_shot_score,
            'penalty_score': penalty_score,
            'free_kick_score': free_kick_score,
            'finishing_score': finishing_score,
            'crossing_score': crossing_score,
            'first_touch_score': first_touch_score,
            'throw_score': throw_score,
            'header_score': header_score,
            'marking_score': marking_score,
            'tackle_score': tackle_score,
            'pass_score': pass_score
        }

    return scores
