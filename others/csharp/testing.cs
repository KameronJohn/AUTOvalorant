using System;
using System.Drawing;
using System.Drawing.Imaging;

public class ScreenshotCapturer
{
    public static void CaptureScreenshot(string filename)
    {
        // Create a bitmap of the screen
        Bitmap screenshot = new Bitmap(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height, PixelFormat.Format32bppArgb);

        // Create a graphics object from the bitmap
        Graphics graphics = Graphics.FromImage(screenshot);

        // Copy the screen contents to the bitmap
        graphics.CopyFromScreen(0, 0, 0, 0, screenshot.Size);

        // Save the bitmap to a file
        screenshot.Save(filename, ImageFormat.Png);

        // Clean up resources
        graphics.Dispose();
        screenshot.Dispose();
    }

    public static void Main()
    {
        CaptureScreenshot("screenshot.png");
        Console.WriteLine("Screenshot captured!");
    }
}
