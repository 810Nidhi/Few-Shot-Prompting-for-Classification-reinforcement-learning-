from groq import generate_response
def reinforcement():
    print("\n REINFORCEMENT LEARNING ACTIVITY")
    prompt=input("Enter a prompt for the AI model(e.g,'Describe the lion')").strip()
    if not prompt:
        print("Please enter a prompt to run the activity")
        return
    initial_response=generate_response(prompt,temperature=0.3,max_tokens=1024)
    print(f"\n Initial AI response:{initial_response} ")
    try:
        rating=int(input("Rate the response from 1(bad) to 5(good):").strip())
        if rating<1 or rating>5:
            print("Invalid Rating.Using 3")
            rating=3
    except ValueError:
        print("Invalid Rating.Using 3")
        rating=3
    feedback=input("Provide feedback for improvement: ").strip()
    imporved_response=f"{initial_response}(Improved with your feedback:{feedback})"
    print(f"\n Improved AI response:{imporved_response} ")
    print("\nReflection")
    print("1.How did the model response improved with your feedback?")
    print("2.How does reinforcement learning help in improving AI models?")
def role_based_prompt_acticity():
    print("ROLE BASED PROMPT ACTIVITY\n")
    category=input("Enter a category (e.g science,history,math): ").strip()
    item=input(f"Enter an item related to {category}: ").strip()
    if not category or not item:
        print("Please fill in both fields to run the activity.")
        return 
    teacher_prompt=f"You are a teacher .Explain{item} in simple terms"
    expert_prompt=f"You are an expert in {category}.Explain {item} in detailed,technical manner."
    teacher_response=generate_response(teacher_prompt,temperature=0.3  ,max_tokens=1024)
    expert_response=generate_response(expert_prompt,temperature=0.3,max_tokens=1024)
    print(f"\n Teacher's perspective {teacher_response}")
    print(f"\n Experts Perspective{expert_response}")
    print(f"\n Reflection")
    print("1.How did the AI response differ between the two perspectives?")
    print("2.How can role based prompt helps tailor AI responses for different audiences?")
def run_activity():
    print("AI Learning Activities")
    print("choose an activity to run:")
    print("1.Reinforcement Learning Activity")
    print("2.Role Based Prompt Activity")
    choice=input(" >").strip()
    if choice=="1":
        reinforcement()
    elif choice=="2":
        role_based_prompt_acticity()
    else:
        print("Invalid choice. Please select 1 or 2.")
if __name__=="__main__":
    run_activity()