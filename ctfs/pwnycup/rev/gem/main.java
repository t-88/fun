// import org.jruby.Ruby;
// import org.jruby.ir.IRScope;
// import org.jruby.ir.runtime.IRRuntimeHelpers;
// import java.io.*;

// public class main {
//    private static final String script_ir = (new StringBuilder()).append("\u0000\u0000\u0000\u0002\u0000\u0000\u0003X\u0016\tF\u0000Ut\u0000\u0001'z\u0007salsa20ÿÿÿÿþ\u0010\u0007main.rb\u0000\"\u0001\u0000S\u0001t\u0000\u0001\u0000t\u0000\u00003\u0001F\nUt\u0000\u0003'z\u0011Enter the input: ÿÿÿÿþ\u0010\u0007main.rb\n\"\u0001\u0001S\u0001t\u0000\u0003\u0000t\u0000\u0002F\u000b%\u0003\u0002S\u0000\u0000t\u0000\u0004%\u0000\u0003t\u0000\u0004\u0000\u0000l\u0004\u0000F\r\"\u0001\u0005S\u0001l\u0004\u0000\u0000l\u0006\u0000F\u000f=t\u0000\u0005s\u0007fUt\u0000\u0007'z\bflag.encÿÿÿÿþ\u0010\u0007main.rb\u000fUt\u0000\b'z\u0002wbÿÿÿÿþ\u0010\u0007main.rb\u000f\u0017\u0000\bt\u0000\u0005ÿÿÿÿýt\u0000\u0007t\u0000\bwS\u0002\u0000t\u0000\u0006F\u0013Ut\u0000\n'z$Flag encrypted and saved to flag.encÿÿÿÿþ\u0010\u0007main.rb\u0013\"\u0001\tS\u0001t\u0000\n\u0000t\u0000\t+t\u0000\t\n\u0007requireÿÿÿÿÿ\u0005printÿÿÿÿÿ\u0004getsÿÿÿÿÿ\u0005chompÿÿÿÿÿ\u0005inputÿÿÿÿÿ\fencrypt_flagÿÿÿÿÿ\u000eencrypted_flagÿÿÿÿÿ\u0004Fileÿÿÿÿÿ\u0004openÿÿÿÿÿ\u0004putsÿÿÿÿÿ\u0010\ft\u0000\u0000ffR\u0001\u0000fÿÿÿÿÿt\u0000\u0000\nl\u0000\u0000t\u0000\u0000\u0000F\u0003Ut\u0000\u0001'z\u0010ftVHDR0k2mLnNhF7ÿÿÿÿþ\u0010\u0007main.rb\u0003Ul\u0001\u0000t\u0000\u0001F\u0004Ut\u0000\u0002'z\bvwAHADYIÿÿÿÿþ\u0010\u0007main.rb\u0004Ul\u0002\u0000t\u0000\u0002F\u0005=t\u0000\u0003s\u0003f#\u0000\u0004t\u0000\u0003\u0002l\u0001\u0000l\u0002\u0000\u0000l\u0005\u0000F\u0006\"\u0000\u0006l\u0005\u0000\u0001l\u0000\u0000\u0000l\u0007\u0000F\u0007+l\u0007\u0000\b\u0005inputÿÿÿÿÿ\u0003keyÿÿÿÿÿ\u0005nonceÿÿÿÿÿ\u0007Salsa20ÿÿÿÿÿ\u0003newÿÿÿÿÿ\u0006cipherÿÿÿÿÿ\u0007encryptÿÿÿÿÿ\u000eencrypted_flagÿÿÿÿÿ\f9L\u0015_GLOBAL_ENSURE_BLOCK_\u0000\ft\u0005\u0000\u0001ff\nl\u0000\u0000t\u0005\u0000\u0001\u0000F\u0010\"\u0000\u0001l\u0000\u0000\u0001l\u0002\u0001\u0000t\u0005\u0001\u0001+t\u0005\u0001\u0001:8L\u0015_GLOBAL_ENSURE_BLOCK_\u0000\u0012t\u0005\u0002\u0001`t\u0005\u0003\u0001\u0002\u0001t\u0005\u0002\u0001.t\u0005\u0003\u00018L\u0007CL1_LBL\u0000\u0003\u0004fileÿÿÿÿÿ\u0005writeÿÿÿÿÿ\u000eencrypted_flagÿÿÿÿÿ\u0003\u0007\u0000\u000b\u0000\u0000\u0002\u0005input\u000eencrypted_flagÿÿÿÿÿÿ\u0000\u0000\u0000\u0000\u0000\u0000\u0000ÿÿ\u0000\u0000?ýffffffffffff\u0000\bÿ\u0000\u0000\u00013\u0002\u0002\u0004\u0000\fencrypt_flagÿÿÿÿÿ\u0000\u0000\u0005\u0005input\u0003key\u0005nonce\u0006cipher\u000eencrypted_flagÿÿÿÿÿÿ\u0000\u0001\u0000\u0000\u0000\u0000\u0000ÿÿ\u0000\u0000 \u0000ffffffffffff\u0000ÿ\u0000\u0000\u0001°ÿ\u0000\u0000\u0002Q\u0000\u000f\u0004\u0001fÿ\u0000\u0001\u0000\u0000\u0000\u0000\u0000ÿ\ropen &|file|1ÿÿÿÿÿ\u0000\u0001\u0001\u0004fileÿÿÿÿÿÿ\u0000\u0001\u0000\u0000\u0000\u0000\u0000ÿÿ\u0000\u0000 \u0000ffffftffffff\u0000ÿ\u0000\u0000\u0002´ÿ\u0000\u0000\u0003.").toString();

//    public static void main(String[] var0) throws IOException {
//     // System.out.println(script_ir); // Print the value of x + y

//     // FileOutputStream outputStream = new FileOutputStream("rub");
//     // byte[] strToBytes = script_ir.getBytes("ISO-8859-1");
//     // outputStream.write(strToBytes);
//     // outputStream.close();    


//       Ruby var1 = Ruby.newInstance();
//       var1.runInterpreter(IRRuntimeHelpers.decodeScopeFromBytes(var1, script_ir.getBytes("ISO-8859-1"), "main.rb"));
//    }

//    public static IRScope loadIR(Ruby var0, String var1) throws Exception {
//       return IRRuntimeHelpers.decodeScopeFromBytes(var0, script_ir.getBytes("ISO-8859-1"), var1);
//    }
// }
    

    import org.jruby.Ruby;
import org.jruby.ir.IRScope;
import org.jruby.ir.runtime.IRRuntimeHelpers;

public class main {
  private static final String script_ir = (new StringBuilder()).append("\000\000\000\002\000\000\000X\007\b\023t\000\000Qt\005\001_\000C\000Qt\000\003'z\013hello world\005UTF-8\020\t./main.rb\000\037\001\000S\001t\000\003t\000\002(t\000\002\001\004puts\bUS-ASCII\001\007\000\004\000\t./main.rb\000\000ÿÿÿÿÿÿ\000\000\000\000\000\000\000ÿÿ\000\000 Efffffffffffff\bI").toString();
  
  public static void main(String[] paramArrayOfString) throws Exception {
    Ruby ruby = Ruby.newInstance();
    ruby.runInterpreter(IRRuntimeHelpers.decodeScopeFromBytes(ruby, script_ir.getBytes("ISO-8859-1"), "main.rb"));
  
  }
  
  public static IRScope loadIR(Ruby paramRuby, String paramString) throws Exception {
    return IRRuntimeHelpers.decodeScopeFromBytes(paramRuby, script_ir.getBytes("ISO-8859-1"), paramString);
  }
}
