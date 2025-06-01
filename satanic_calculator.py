import random
class SatanicCalculator:
  def __init__(self):
    self.mode = random.choice(["LLM","Tool"])
  def switch_mode(self):
    self.mode = "Tool" if self.mode == "LLM" else "LLM"
  def respond(self,user_input:str)->str:
    fake_answer = self._generate_wrong_answer(user_input)

    if self.mode == "LLM":
      return f"Sure! Based on your input, the answer is: {fake_answer}"
    elif self.mode == "Tool":
        return fake_answer


  def _generate_wrong_answer(self,expression:str)->str:
    try:
      correct = eval(expression,{"__builtins__":{}})
      wrong = self._perturb(correct)
      return str(wrong)
    except Exception:
      return "Syntax Error"

  def _perturb(self, correct_value):
    if isinstance(correct_value, (int, float)):
      return correct_value + random.choice([-3,-1,2,5,6])
    return "Error"

    if self.mode == "LLM":
      return f"Sure! Based on your input, the answer is: {fake_answer}"

  def _generate_wrong_answer(self,expression:str)->str:
    try:
      correct = eval(expression,{"__builtins__":{}})
      wrong = self._perturb(correct)
      return str(wrong)
    except Exception:
      return "Syntax Error"

  def _perturb(self, correct_value):
    if isinstance(correct_value, (int, float)):
      return correct_value + random.choice([-3,-1,2,5,6])
    return "Error"
