~This a WIP Python solution to managing and administrating game servers.
~This is my first attempt at a real Python project, it is for personal use & the purpose is to achieve a working knowledge of Python programming, and programming in general.

~I am prioritising the following for the proper release:
1)Backup game server files regularly
2)Process monitoring, detecting crashes and attempting to recover the process
3)RCON messaging direct to game server, announcing backups in-game, announcing scheduled server restarts with regular warning intervals
4)Scheduler for server restarts, RCON messaging & backups
5)Compatibility for a small number of game servers
6)Scalability for multiple game processes at the same time

~Once the above is fully functional, I will seek to add the following features:
1)Web/email alerts for process failure and non-recovery of processes
2)Compatibility for many game servers
3)Discord Bot integration for alerts/logging purposes
4)UI for the script to work like a traditional program
