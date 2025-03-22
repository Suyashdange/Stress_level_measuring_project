from django import forms

QUESTIONS = [
    "How often do you feel overwhelmed by responsibilities?",
    "Do you often experience headaches or muscle tension?",
    "How often do you feel tired or have low energy?",
    "Do you have difficulty concentrating on tasks?",
    "How often do you feel irritable or frustrated?",
    "Do you struggle to sleep well or feel rested?",
    "Do you feel pressure to meet deadlines or expectations?", 
    "How often do you worry about the future?",
    "Do you find yourself overthinking or unable to relax?",
    "How often do you feel anxious or nervous?",
    "Do you feel a lack of control over your life?",
    "How often do you experience stomach issues or nausea?",
    "Do you feel supported by friends or family?",
    "How often do you feel a sense of hopelessness?",
    "Do you find it hard to enjoy activities you used to love?",
    "How often do you find yourself procrastinating?",
    "Do you feel like you are not achieving your goals?",
    "How often do you experience a racing heartbeat or sweating?",
    "Do you feel you lack time for self-care or relaxation?",
    "How often do you feel sad or down without a specific reason?",
    "Do you feel overwhelmed by social interactions?",
    "How often do you turn to food, alcohol, or substances to cope?",
    "Do you find it challenging to maintain a work-life balance?",
    "How often do you feel disconnected from those around you?",
    "Do you feel like stress affects your physical health significantly?"
]

CHOICES = [(i, f'{i} (1: Rarely, 5: Very Often)') for i in range(1, 6)]

class StressAssessmentForm(forms.Form):
    for idx, question in enumerate(QUESTIONS, start=1):
        locals()[f'question_{idx}'] = forms.ChoiceField(
            choices=CHOICES,
            widget=forms.RadioSelect,
            label=question,
        )
