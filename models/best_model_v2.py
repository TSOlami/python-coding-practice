import math


class Reward:
    def __init__(self, verbose=False, track_time=False):
        self.prev_speed = 0
        self.verbose = verbose
        self.track_time = track_time

    def reward_function(self, params):
        # Extract parameters
        all_wheels_on_track = params['all_wheels_on_track']
        speed = params['speed']
        progress = params['progress']
        heading = params['heading']
        waypoints = params['waypoints']
        closest_waypoints = params['closest_waypoints']
        
        # Calculate the reward
        reward = 1e-3  # Small reward by default
        
        # Reward for keeping all wheels on track
        if all_wheels_on_track:
            reward += 1.0
        
        # Reward for progress
        reward += progress / 100.0
        
        # Reward for maintaining speed (ensure the car is above a speed threshold)
        SPEED_THRESHOLD = 3.5
        if speed >= SPEED_THRESHOLD:
            reward += 2.0
        
        # Reward for improving speed
        if speed > self.prev_speed:
            reward += 2.0
        
        # Penalty for incorrect heading
        next_waypoint = waypoints[closest_waypoints[1]]
        prev_waypoint = waypoints[closest_waypoints[0]]
        track_direction = self.calculate_track_direction(prev_waypoint, next_waypoint)
        direction_diff = abs(track_direction - heading)
        
        DIRECTION_THRESHOLD = 10.0
        if direction_diff > DIRECTION_THRESHOLD:
            reward *= 0.5

        # Update previous speed
        self.prev_speed = speed
        
        # Verbose output
        if self.verbose:
            print(f"Reward: {reward}, Speed: {speed}, Progress: {progress}, Heading: {heading}, Direction Diff: {direction_diff}")

        return float(reward)

    @staticmethod
    def calculate_track_direction(prev_waypoint, next_waypoint):
        
        track_direction = math.atan2(next_waypoint[1] - prev_waypoint[1], next_waypoint[0] - prev_waypoint[0])
        track_direction = math.degrees(track_direction)
        return track_direction


reward_object = Reward(verbose=True)

def reward_function(params):
    return reward_object.reward_function(params)
