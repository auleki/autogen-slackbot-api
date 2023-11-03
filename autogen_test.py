import autogen

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
    human_input_mode="TERMINATE",
    code_execution_config={"work_dir":"_output", "use_docker":"python:3" },
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE")
)

dump_command = " and store the output the final result into a text file called result.txt"

def talk_to_autogen():
    #to initiate conversation with user
    user_proxy.initiate_chat(assistant, message="Define what an equator is")
    msg = user_proxy.generate_reply(assistant)
    print("Last message is:")
    print(msg)

talk_to_autogen()

#to enable logging
autogen.ChatCompletion.start_logging()
