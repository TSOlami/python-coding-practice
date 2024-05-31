import math


class Reward:
    def __init__(self):
        self.prev_speed = 0

reward_object = Reward()

def reward_function(params):
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    track_width = params['track_width']
    speed = params['speed']
    progress = params['progress']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    distance_from_center = params['distance_from_center']
    heading = params['heading']

    # Give a very low reward by default
    reward = 1e-3

    # Give a high reward if no wheels go off the track
    if all_wheels_on_track:
        reward += 1.0

    # Reward for progress
    reward += progress / 100.0

    # Reward for maintaining high speed (ensure the car is above a speed threshold)
    SPEED_THRESHOLD = 3.5
    if speed >= SPEED_THRESHOLD:
        reward += 2.0

    # Reward for improving speed (acceleration)
    acceleration = speed - reward_object.prev_speed
    if acceleration > 0:
        reward += 2.0  # Increased reward for accelerating

    # Determine the direction of the turn using the closest waypoints
    next_waypoint = waypoints[closest_waypoints[1]]
    prev_waypoint = waypoints[closest_waypoints[0]]
    track_direction = math.atan2(next_waypoint[1] - prev_waypoint[1], next_waypoint[0] - prev_waypoint[0])
    track_direction = math.degrees(track_direction)

    # Reward for staying close to the optimal path
    # Calculate the difference between the track direction and the car's heading
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    # Penalize if the heading direction is too far off the track direction
    DIRECTION_THRESHOLD = 10.0
    if direction_diff > DIRECTION_THRESHOLD:
        reward *= 0.5

    # Update previous speed
    reward_object.prev_speed = speed

    # Always return a float value
    return float(reward)