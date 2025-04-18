class Dog:
    """A virtual dog pet class with name Simba"""
    
    def __init__(self):
        """Initialize Simba with default stats"""
        self.name = "Simba"
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
        self.breed = "Golden Retriever"
        self.age = 1  # in years
    
    def eat(self):
        """Simba eats dog food"""
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        return f"🍖 {self.name} wolfs down his dog food!"
    
    def sleep(self):
        """Simba takes a nap"""
        self.energy = min(10, self.energy + 5)
        return f"😴 {self.name} curls up and snores softly..."
    
    def play(self):
        """Simba plays with toys"""
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            return f"🎾 {self.name} excitedly chases his ball!"
        return f"😪 {self.name} is too tired to play right now"
    
    def bark(self):
        """Special dog method - Simba barks"""
        return f"🐕 {self.name} says: Woof! Woof!"
    
    def get_status(self):
        """Return Simba's current status"""
        status = [
            f"\n{self.name}'s Status ({self.breed}, Age: {self.age})",
            f"Hunger:    {'♥' * self.hunger}{'♡' * (10 - self.hunger)} {self.hunger}/10",
            f"Energy:    {'♦' * self.energy}{'♢' * (10 - self.energy)} {self.energy}/10",
            f"Happiness: {'☺' * self.happiness}{'☹' * (10 - self.happiness)} {self.happiness}/10"
        ]
        return "\n".join(status)
    
    def train(self, trick):
        """Teach Simba a new dog trick"""
        self.tricks.append(trick)
        self.happiness = max(0, self.happiness - 1)
        self.energy = max(0, self.energy - 1)
        return f"🎓 {self.name} learned to {trick}! Good boy!"
    
    def show_tricks(self):
        """Show all tricks Simba knows"""
        if not self.tricks:
            return f"{self.name} hasn't learned any tricks yet. Time for training!"
        return f"{self.name} knows: {', '.join(self.tricks)}"
    
    def wag_tail(self):
        """Special dog behavior"""
        self.happiness = min(10, self.happiness + 1)
        return f"~{self.name} wags his tail happily~"