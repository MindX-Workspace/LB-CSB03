print("Chào mừng bạn đến với trò chơi đoán đúng sai!\nBạn đã sẵn sàng chưa? Bắt đầu thôi nào!\n")

questions_and_answers = [
    ("Python là ngôn ngữ lập trình?", "đúng"),
    ("Trái Đất hình vuông?", "sai"),
    ("Năm 2024 là năm nhuận?", "đúng"),
    ("Con bò có thể bay?", "sai")
]

score = 0

for question, correct_answer in questions_and_answers:
    print(question)
    user_answer = input("Câu trả lời của bạn là (đúng/sai): ").lower()
    
    if user_answer == correct_answer:
        print("Chính xác!")
        score += 1
    else:
        print("Chưa chính xác!")

print(f"\nBạn đã trả lời đúng {score} câu.")
print("Cảm ơn bạn đã tham gia trò chơi!")