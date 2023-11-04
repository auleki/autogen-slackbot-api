import autogen
import json

config_list = autogen.config_list_from_json(env_or_file="OAI_CONFIG_LIST")

assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config={
        "seed": 41,
        "config_list": config_list
        }
    )

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    max_consecutive_auto_reply=10,
    human_input_mode="TERMINATE",
    code_execution_config={"work_dir":"_output", "use_docker":"python:3" },
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE")
)

def talk_to_autogen(task):
    #to initiate conversation with user
    user_proxy.initiate_chat(assistant, message=task)
    handleChatMessages(user_proxy.chat_messages)

# to parse messages and make them more readable
def handleChatMessages(messages):
    print("all-messages")
    #formatted_data = json.dumps(messages, indent=4)
    # value_of_msgs = messages.values()
    # print(value_of_msgs)
    all_msgs = [item for sublist in messages.values() for item in sublist]
    print(all_msgs)
    # for item in all_msgs:
    #     print(item)
    # for msg in messages:
    #     for key, values in msg.items():
    #         print(f"{key}")
    #         for value in values:
    #             print(f"   {value['role']}: {value['content']}")

task = "What is the best time to plant apples?"
#talk_to_autogen(task)

#to enable logging
autogen.ChatCompletion.start_logging()
