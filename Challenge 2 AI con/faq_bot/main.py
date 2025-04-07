# faq_bot/main.py

from .graph import build_graph

graph = build_graph()

def main():
    print("🤖 Welcome to the LangGraph FAQ Bot!")
    while True:
        user_input = input("Ask your question (type 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        result = graph.invoke({"question": user_input})
        print("Bot:", result["answer"])

if __name__ == "__main__":
    main()
