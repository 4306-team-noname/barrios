. .agent > /dev/null
ps -p $SSH_AGENT_PID | grep ssh-agent > /dev/null || {
        ssh-agent > .agent
        . .agent > /dev/null
}
