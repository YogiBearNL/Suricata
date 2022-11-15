# Suricata setup

This repository contains a Powerpoint with information about howto setup Suricata.
Also a way to visualise the events in Splunk. Including statistics about the performance of Suricata; handling incoming packets.

## Splunk TAs

Within the folder splunk/etc/apps you can find the 2 Splunk TAs needed to visualise the events
You have to monitor the eve.json file using inputs.conf
Example inputs.conf

```yaml
[monitor:///var/log/suricata/eve.json]
disabled = 0
sourcetype = suricata
index = suricata
# Set time-zone in SourceType
TZ = UTC

[monitor:///var/log/suricata/stats.log]
disable = 0
sourcetype = suricata:stats
index = staging
# Set time-zone in SourceType
TZ = UTC
```

Within the TA-Suricata (within the repository) the timezone UTC is set for the sourcetype suricata.

default/props.conf:

```yaml
[suricata]
.....
TZ = UTC
....
```
