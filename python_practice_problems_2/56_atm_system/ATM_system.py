#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:20:54 2023

@author: johnmorgan
"""

# Enumerations
class ATMState(enum.Enum):
  Idle = 1
  HasCard = 2
  SelestionOption = 3
  Withdraw = 4
  TransferMoney = 5
  BalanceInquiry = 6
  
class User:
  def __init__(self, card, account):
    self.__card = card
    self.__account = account

class ATMCard:
  def __init__(self, cardNumber, customerName, cardExpiryDate):
    self.__cardNumber = cardNumber
    self.__customerName = customerName
    self.__cardExpiryDate = cardExpiryDate
    self.__pin = pin
    
from abc import ABC, abstractmethod
class Bank:
  def __init__(self, name, bankCode, availableBalance):
    self.__name = name
    self.__bankCode = bankCode
    self.__availableBalance = availableBalance

  def getBankCode(self):
    pass

  def addATM(self):
    pass

class BankAccount:
  def __init__(self, accountNumber, totalBalance, availableBalance):
    self.__accountNumber = accountNumber
    self.__totalBalance = totalBalance
    self.__availableBalance = availableBalance

  def getAvailableBalance(self):
    pass
    
class SavingAccount(BankAccount):
  def __init__(self, accountNumber, totalBalance, availableBalance):
    super().__init__(accountNumber, totalBalance, availableBalance)
  
  def withdrawLimit(self):
    pass

class CurrentAccount(BankAccount):
  def __init__(self, accountNumber, totalBalance, availableBalance):
    super().__init__(accountNumber, totalBalance, availableBalance)
  
  def withdrawLimit(self):
    pass

class CardReader:
  def readCard():
    pass

class CashDispenser:
  def dispenseCash():
    pass

class Keypad:
  def getInput():
    pass

class Screen:
  def showMessage():
    pass

class Printer:
  def printReceipt():
    pass

from abc import ABC, abstractmethod
class ATMState(ABC):
  @abstractmethod
  def insertCard(self, atm, card):
    pass

  @abstractmethod
  def authenticatePin(self, atm, card, pin):
    pass

  @abstractmethod
  def selectOperation(self, atm, card, transactionType):
    pass

  @abstractmethod
  def cashWithdrawal(self, atm, card, withdrawAmount):
    pass

  @abstractmethod
  def displayBalance(self, atm, card):
    pass

  @abstractmethod
  def transferMoney(self, atm, card, accountNumber, transferAmount):
    pass

  @abstractmethod
  def returnCard(self):
    pass

  @abstractmethod
  def exit(self, atm):
    pass

class IdleState(ATMState):
  def insertCard(self, ATM atm, ATMCard card):
    pass

  def returnCard(self):
    pass

  def exit(self, ATM atm):
    pass

class HasCardState(ATMState):
  def authenticatePin(self, atm, card, pin):
    pass

  def returnCard(self):
    pass

  def exit(self, ATM atm):
    pass
    
class SelectOperationState(ATMState):
  def selectOperation(self, atm, card, transactionType):
    pass

  def returnCard(self):
    pass

  def exit(self, ATM atm):
    pass

class CheckBalanceState(ATMState):
  def displayBalance(self, atm, card):
    pass

  def returnCard(self):
    pass

  def exit(self, ATM atm):
    pass

class CashWithdrawalState(ATMState):
  def cashWithdrawal(self, atm, card, withdrawAmount):
    pass

  def returnCard(self):
    pass

  def exit(self, ATM atm):
    pass

class TransferMoneyState(ATMState):
  def transferMoney(self, atm, card, accountNumber, transferAmount):
    pass

  def returnCard(self):
    pass

  def exit(self, ATM atm):
    pass

class ATM:
  def __init__(self, currentATMState, atmBalance, noOfHundredDollarBills,
               noOfFiftyDollarBills, noOfTenDollarBills):
    self.__currentATMState = currentATMState
    self.atmBalance = atmBalance
    self.noOfHundredDollarBills = noOfHundredDollarBills
    self.noOfFiftyDollarBills = noOfFiftyDollarBills
    self.noOfTenDollarBills = noOfTenDollarBills

  def displayCurrentState(self):
    pass

  def initializeATM(self, atmBalance, noOfHundredDollarBills,
                    noOfFiftyDollarBills, noOfTenDollarBills):
    pass

class ATMRoom:
  def __init__(self, atm, user):
    self.__atm = atm
    self.user = user