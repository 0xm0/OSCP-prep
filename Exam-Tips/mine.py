If you're stuck in the lab/exam unable to run exloit, find vuln.. etc. 
Look for the product name with association to vulnhub or Hackthebox 
> sometimes these are 1:1 as the lab practice for example apache + postfix + vulnhub > google result shows dedicated write up for this exact match.

Recon tips:
If a specific web app doesn't seem to have any directories exposed - 
try to test the name of the domain/subdomain as a potential directory.
OR
CMS name/ forum name/ users / other indicators. 
e.g. > target.e231.com/e231 or  target.e231.com/target

Viewing target files
If  can't open or view 
try cat -A 
try with vim 
if viewing doesnt work at all - download to local machine 


Exam tipsfrom reddit

1. Do the buffer overflow first
A: enumerate more or google a way to enumerate the specific service differently
B: think of how what you enumerated > can you chain together to get a shell or sensitive information (service_xyz vuln + service_ttt vuln = the specfic exploit that works 
C: read the exploit you're using and see if it needs editing (based on target info)
3. I've seen alot of posts about how the exam machines are different than the lab, and from what I can tell they're different because you sometimes have to piece together more information. 
Many of the lab machines follow a simple formula of enumerate services --> searchsploit the service for vulns --> use the exploit to get a low priv shell --> privelege escalation shenanigans. 
However, in the exam machines it sometimes isn't as simple as just searchsploiting a potentially vulnerable service and then exploiting it.
4. Realize when your going down a rabbit hole.
5. Have a solid methodology for testing.

Offsec won't make you reinvent the wheel so to speak. In other words you won't need super complicated exploits to get root. The type of exploits that work on these machines will make you think "why didn't I think of that sooner?" But at the same time, the answer isn't right in your face.
