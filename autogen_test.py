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
    human_input_mode="ALWAYS",
    code_execution_config={"work_dir": "_output", "use_docker": "python3" },
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE")
)

#to initiate conversation with user
user_proxy.initiate_chat(assistant, message="Besides space rockets, how can I get to the moon?")

#to enable logging
autogen.ChatCompletion.start_logging()
