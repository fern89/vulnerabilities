# Unauth 0-click RCE for BlackMamba C2 framework
https://github.com/loseys/BlackMamba

At https://github.com/loseys/BlackMamba/blob/main/clientui/ui_main.py#L2366 , we observe an unsanitized call to exec(). This allows an attacker to trivially gain remote code execution.

This exploit works 0-click, and will activate every time the operator starts up the C2 panel (basically free persistence of a sort).

The hardest part of exploiting this, was because spaces and commas are all filtered out. So we need to get a bit more creative to give ourselves a revshell. The POC demonstrates an example of this.
