
import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;

public class TCPClient {
	public static final String IP_ADDR = "192.168.0.188";//服务器地址 
	public static final int PORT = 23567;//服务器端口号  
	
    public static void main(String[] args) {  
        System.out.println("client starting...");  
        System.out.println("client will exit while \"OK\" was received from server\n"); 
        System.out.println("IP_ADDR: " + IP_ADDR + ", PORT: " + PORT + "\n"); 
        while (true) {  
        	Socket socket = null;
        	try {
        		//创建一个流套接字并将其连接到指定主机上的指定端口号
	        	socket = new Socket(IP_ADDR, PORT);  
	              
	            //读取服务器端数据  
	            DataInputStream input = new DataInputStream(socket.getInputStream());  
	            //向服务器端发送数据  
	            DataOutputStream out = new DataOutputStream(socket.getOutputStream());  
	            System.out.print("请输入: \t");  
	            String str = new BufferedReader(new InputStreamReader(System.in)).readLine();  
	            out.writeUTF(str);  
	              
	            String ret = input.readUTF();   
	            System.out.println("服务器端返回过来的是: " + ret);  
	            // 如接收到 "OK" 则断开连接  
	            if ("OK".equals(ret)) {  
	                System.out.println("客户端将关闭连接");  
	                Thread.sleep(500);  
	                break;  
	            }  
	            
	            out.close();
	            input.close();
        	} catch (Exception e) {
        		System.out.println("客户端异常:" + e.getMessage()); 
        	} finally {
        		if (socket != null) {
        			try {
						socket.close();
					} catch (IOException e) {
						socket = null; 
						System.out.println("客户端 finally 异常:" + e.getMessage()); 
					}
        		}
        		else
					break;
        	}
        }  
    }  
}  
