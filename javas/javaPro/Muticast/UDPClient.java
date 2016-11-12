import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.MulticastSocket;


public class UDPClient {
    public static void main(String args[]) throws Exception
    {
		//UDP sender
		System.out.println("UDP Client starting...");
		int port = 6789;  
		String sendMessage="hello multicast";  
		InetAddress inetAddress = InetAddress.getByName("228.5.6.7");  
		DatagramPacket datagramPacket = new DatagramPacket(sendMessage.getBytes(), sendMessage.length(), inetAddress, port);  
		MulticastSocket multicastSocket = new MulticastSocket(); //it is client, it won't join group
		multicastSocket.send(datagramPacket);
	}
}
