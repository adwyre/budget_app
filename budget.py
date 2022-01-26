class Category:
  def __init__(self, name):
    self.name= name
    self.ledger = list()
    self.total = [0]

  def __str__(self):  
    budget_string= f"{self.name:*^30}\n"
    for item in self.ledger:
      budget_string += f"{item['description'][0:23]:23}{item['amount']:>7.2f}\n"
    budget_string = budget_string + f"Total: " + str(self.get_balance())
    return budget_string


  def deposit(self, amount, description=''):
    self.ledger.append({"amount": amount, "description": description})
    self.total.append(float(amount))
  def withdraw(self, amount, description=''):
    if (self.check_funds(amount)):
      self.ledger.append({"amount": -amount, "description": description})
      self.total.append(float(-amount))
      return True
    else:
      return False
  def get_balance(self):
    return round(sum(self.total),2)
  def transfer(self, amount, category): 
    if (self.check_funds(amount)):
      self.withdraw(amount, 'Transfer to ' + category.name)
      category.deposit(amount,'Transfer from ' + self.name)  
      return True
    else: 
      return False
  def check_funds(self, amount):
    if (amount > self.get_balance()):
      return False
    else:
      return True
  
def create_spend_chart(categories):
  chart= "Percentage spent by category\n"
  percentList = []
  totalSpent= 0
 
  #get percent
  for category in categories:
    wthdrAmount = -(category.ledger[1]["amount"])
    totalSpent += wthdrAmount
  for category in categories:
    wthdrAmount = -(category.ledger[1]["amount"])
    percentList.append(int((wthdrAmount/totalSpent)*100))

  #make bars
  top=100
  while top >= 0:
    i = 0
    if len(str(top)) < 3:
      while i < (3-len(str(top))):
        chart += (' ')
        i += 1
    chart = chart + str(top) + '|'
    i = 0
    while i < len(categories):
      if (percentList[i] >= top):
        chart += " o "
      else: chart += "   "
      i += 1
    chart += " \n"
    top -= 10
  #line
  chart = chart + "    " + ("---"* len(categories)) + "-"
  #categories
  maxLength= 0
  for category in categories:
    if len(category.name) > maxLength:
      maxLength = len(category.name)
  i = 0
  while i < maxLength:
    chart += "\n    "
    for category in categories:
      try:
        chart = chart + ' ' + category.name[i] + ' '
      except:
        chart += "   "
    chart += " "
    i += 1
  chart 
  return chart

