"""Lab2 part1 topology 
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and ovses
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )

        ovsA = self.addSwitch( 's1' )
        ovsB = self.addSwitch( 's2' )
	ovsC = self.addSwitch( 's3' ) 
	ovsD = self.addSwitch( 's4' )
	ovsE = self.addSwitch( 's5' )
  
        # Add links
        self.addLink( leftHost, ovsA )
	self.addLink( ovsA, ovsB )
	self.addLink( ovsA, ovsC )
	self.addLink( ovsB, ovsD )
	self.addLink( ovsB, ovsE )
	self.addLink( ovsE, ovsD )
	self.addLink( ovsE, ovsC )
	self.addLink( ovsC, ovsD )
	self.addLink( ovsD, rightHost )

topos = { 'mytopo': ( lambda: MyTopo() ) }
