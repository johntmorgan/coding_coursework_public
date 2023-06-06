#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 14:25:35 2023

@author: johnmorgan
"""

from enum import Enum
from abc import ABC, abstractmethod

class Address:
  def __init__(self, zip_code, street_address, city, state, country):
    self.__zip_code = zip_code
    self.__street_address = street_address
    self.__city = city
    self.__state = state
    self.__country = country

class MatchResult(Enum):
  LIVE = 1 
  BAT_FIRST_WIN = 2
  FIELD_FIRST_WIN = 3
  DRAW = 4
  CANCELED = 5

class UmpireType(Enum):
  FIELD = 1 
  RESERVED = 2
  THIRD_UMPIRE = 3

class WicketType(Enum):
  BOLD = 1 
  CAUGHT = 2
  STUMPED = 3
  RUN_OUT = 4
  LBW = 5
  RETIRED_HURT = 6
  HIT_WICKET = 7
  OBSTRUCTING = 8
  HANDLING = 9

class BallType(Enum):
  NORMAL = 1 
  WIDE = 2
  NO_BALL = 3
  WICKET = 4

class RunType(Enum):
  NORMAL = 1 
  FOUR = 2
  SIX = 3
  LEG_BYE = 4
  BYE = 5
  NO_BALL = 6
  OVERTHROW = 7
  
class PlayingPosition(Enum):
  BATTING = 1 
  BOULING = 2
  ALL_ROUNDER = 3
  
class Admin:
  def __init__(self):
    pass

  def add_player(self, player):
    pass  
  def add_team(self, team):
    pass
  def add_match(self, match):
    pass 
  def add_tournament(self, tournament):
    pass
  def add_stats(self, stats):
    pass 
  def add_news(self, news):
    pass

class Player:
  def __init__(self, name, age, country, position, teams, stat):
    self.__name = name
    self.__age = age
    self.__country = country
    self.__position = position
    self.__teams = teams
    self.__stat = stat

class Coach:
  def __init__(self, name, age, country, teams):
    self.__name = name
    self.__age = age
    self.__country = country
    self.__teams = teams

class Umpire:
  def __init__(self, name, age, country):
    self.__name = name
    self.__age = age
    self.__country = country

  def assign_match(match):
    pass

class Run:
  def __init__(self, total_runs, _type, scored_by):
    self.__total_runs = total_runs
    self.___type = _type
    self.__scored_by = scored_by

class Ball:
  def __init__(self, balled_by, played_by, _type, runs, wicket):
    self.__balled_by = balled_by
    self.__played_by = played_by
    self.___type = _type
    self.__runs = runs
    self.__wicket = wicket
    
  def add_commentary(commentary):
    pass

class Wicket:
  def __init__(self, _type, player_out, balled_by, caught_by, runout_by,
               stumped_by):
    self.___type = _type
    self.__player_out = player_out
    self.__balled_by = balled_by
    self.__caught_by = caught_by
    self.__runout_by = runout_by
    self.__stumped_by = stumped_by

class Over:
  def __init__(self, number, bowler, total_score, overs):
    self.__number = number
    self.__bowler = bowler
    self.__total_score = total_score
    self.__overs = overs
    
  def add_ball(ball):
    pass

class Innings:
  def __init__(self, bowling, address, start_time, end_time, total_scores,
               total_wickets, overs):
    self.__bowling = bowling
    self.__address = address
    self.__start_time = start_time
    self.__end_time = end_time
    self.__total_scores = total_scores
    self.__total_wickets = total_wickets
    self.__overs = overs
    
  def add_over(over):
    pass

class Match(ABC):
  def __init__(self, start_time, result, total_overs, teams, innings, toss_win,
               umpires, stadium, commentators, stats):
    self.__start_time = start_time
    self.__result = result
    self.__total_overs = total_overs
    self.__teams = teams
    self.__innings = innings
    self.__toss_win = toss_win
    self.__umpires = umpires
    self.__stadium = stadium
    self.__commentators = commentators
    self.__stats = stats

  @abstractmethod
  def assign_stadium(self, stadium):
    pass
  def assign_umpire(self, umpire):
    pass

class T20(Match):
  def __init__(self, start_time, result, total_overs, teams, innings, toss_win,
               umpires, stadium, commentators, stats):
    super().__init__(start_time, result, total_overs, teams, innings, toss_win,
                     umpires, stadium, commentators, stats)

  def assign_stadium(self, stadium):
    pass
  def assign_umpire(self, umpire):
    pass

class Test(Match):
  def __init__(self, start_time, result, total_overs, teams, innings, toss_win,
               umpires, stadium, commentators, stats):
    super().__init__(start_time, result, total_overs, teams, innings, toss_win,
                     umpires, stadium, commentators, stats)
  
  def assign_stadium(self, stadium):
    pass
  def assign_umpire(self, umpire):
    pass

class ODI(Match):
  def __init__(self, start_time, result, total_overs, teams, innings, toss_win,
               umpires, stadium, commentators, stats):
    super().__init__(start_time, result, total_overs, teams, innings, toss_win,
                     umpires, stadium, commentators, stats)
 
  def assign_stadium(self, stadium):
    pass
  def assign_umpire(self, umpire):
    pass

class Team:
  def __init__(self, name, players, coach, news, stats):
    self.__name = name
    self.__players = players
    self.__coach = coach
    self.__news = news
    self.__stats = stats

  def add_squad(squad):
    pass
  def add_player(player):
    pass
  def add_news(news):
    pass


class TournamentSquad:
  def __init__(self, players, tournament, stats):
    self.__players = players
    self.__tournament = tournament
    self.__stats = stats

  def add_player(player):
    pass

class Playing11:
  def __init__(self, players):
    self.__players = players

  def add_player(player):
    pass

class Tournament:
  def __init__(self, start_date, teams, matches, points):
    self.__start_date = start_date
    self.__teams = teams
    self.__matches = matches
    self.__points = points

  def add_team(team):
    None
  def add_match(match):
    None

class PointsTable:
  def __init__(self, team_points, match_results, tournament, last_updated):
    self.__team_points = team_points
    self.__match_results = match_results
    self.__tournament = tournament
    self.__last_updated = last_updated

class Stadium:
  def __init__(self, name, location, max_capacity):
    self.__name = name
    self.__location = location
    self.__max_capacity = max_capacity

class Commentator:
  def __init__(self, name):
    self.__name = name

  def assign_match(match):
    None

class Commentary:
  def __init__(self, text, created_at, commentator):
    self.__text = text
    self.__created_at = created_at
    self.__commentator = commentator

class News:
  def __init__(self, date, text, image, team):
    self.__date = date
    self.__text = text
    self.__image = image
    self.__team = team

class Stat(ABC):
  def __init__(self):
    None

  @abstractmethod
  def update_stats(self):
    None

class PlayerStat(Stat):
  def __init__(self, ranking, best_score, best_wicket_count,
               total_matches_played, total100s, total_hattricks):
    self.__ranking = ranking
    self.__best_score = best_score
    self.__best_wicket_count = best_wicket_count
    self.__total_matches_played = total_matches_played
    self.__total100s = total100s
    self.__total_hattricks = total_hattricks

  def update_stats(self):
    None

class MatchStat(Stat):
  def __init__(self, win_percentage, top_batsman, top_bowler):
    self.__win_percentage = win_percentage
    self.__top_batsman = top_batsman
    self.__top_bowler = top_bowler
  
  def update_stats(self):
    None

class TeamStat(Stat):
  def __init__(self, total_sixes, total_fours, total_reviews):
    self.__total_sixes = total_sixes
    self.__total_fours = total_fours
    self.__total_reviews = total_reviews
  
  def update_stats(self):
    None

