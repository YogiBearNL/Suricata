#!/usr/bin/env python
###############################################################################
#
# Copyright (C) 2013-2014 Cisco and/or its affiliates. All rights reserved.
#
# THE PRODUCT AND DOCUMENTATION ARE PROVIDED AS IS WITHOUT WARRANTY OF ANY
# KIND, AND CISCO DISCLAIMS ALL WARRANTIES AND REPRESENTATIONS, EXPRESS OR
# IMPLIED, WITH RESPECT TO THE PRODUCT, DOCUMENTATION AND RELATED MATERIALS
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY
# AND FITNESS FOR A PARTICULAR PURPOSE; WARRANTIES ARISING FROM A COURSE OF
# DEALING, USAGE OR TRADE PRACTICE; AND WARRANTIES CONCERNING THE
# NON-INFRINGEMENT OF THIRD PARTY RIGHTS.
#
# IN NO EVENT SHALL CISCO BE LIABLE FOR ANY DAMAGES RESULTING FROM LOSS OF
# DATA, LOST PROFITS, LOSS OF USE OF EQUIPMENT OR LOST CONTRACTS OR FOR ANY
# SPECIAL, INDIRECT, INCIDENTAL, PUNITIVE, EXEMPLARY OR CONSEQUENTIAL
# DAMAGES IN ANY WAY ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THE PRODUCT OR DOCUMENTATION OR RELATING TO THIS
# AGREEMENT, HOWEVER CAUSED, EVEN IF IT HAS BEEN MADE AWARE OF THE
# POSSIBILITY OF SUCH DAMAGES.  CISCO'S ENTIRE LIABILITY TO LICENSEE,
# REGARDLESS OF THE FORM OF ANY CLAIM OR ACTION OR THEORY OF LIABILITY
# (INCLUDING CONTRACT, TORT, OR WARRANTY), SHALL BE LIMITED TO THE LICENSE
# FEES PAID BY LICENSEE TO USE THE PRODUCT.
#
################################################################################
#
#  ChangeLog
#
#   1.0  - CGrady - ORIGINAL RELEASE WITH INTRODUCTION OF SPLUNK APP
#
################################################################################


################################################################################
#  Import modules
################################################################################

import base64, struct, sys

#import cherrypy
#import splunk.appserver.mrsparkle.controllers as controllers
#from splunk.appserver.mrsparkle.lib.decorators import expose_page
#from splunk.appserver.mrsparkle.lib.routes import route


################################################################################
#  tools class
################################################################################

event_id = 'abCD'
packet   = "AFBWRu/6dIPvTq5LCABFAABA6RFAADgGABJDz1/mJvKO7eIOABaeZsqomiWIpIAYAfZ+5AAAAQEICsipdRkKbpO1U1NILTIuMC1Hbw0K".encode("ascii")
payload  = 'U1NILTIuMC1Hbw0K'
    
# If we have an event ID and PCAP, then...
if (len(event_id) and len(packet)):
      
  # Add the PCAP header to the packet
  packet_binary = base64.decodebytes(packet)

  # PCAP header
  # pcap = 'd4c3b2a1020004000000000000000000ffff010001000000' + packet_binary
  pcap = struct.pack("IHHIIII",
    0xa1b2c3d4,  # Magic
    2,           # Major
    4,           # Minor
    0,           # This zone
    0,           # Sigfigs
    0xffffffff,  # Snaplen
    1            # DataLink type (Ethernet)
  )
  pcap = pcap + packet_binary

  print(pcap)
  #pcapbinary = base64.decodestring(pcap)
      
  # Define the output as the decoded PCAP
  try:
    output = pcap
  except TypeError as detail:
        # We have an error
    error = 1
    output = 'Something is wrong with the pcap string: %s' % detail
      
# If we don't have what we need, then...
else:
   error = 1
   output = 'We do not have the information we want.'
    
# If we had an error, we'll be printing just text
if (error):
   cherrypy.response.headers['Content-Type'] = 'text/plain'
      
# Otherwise we're providing a PCAP
else:
   cherrypy.response.headers['Content-Type'] = 'application/vnd.tcpdump.pcap'
   cherrypy.response.headers['Content-Disposition'] = 'attachment; filename=%s.pcap' % event_id
    

