using System.Windows;
using Microsoft.Win32; // Pro práci s registrami

namespace LogApp;

public partial class App
{
    public App()
    {
        InitializeComponent();
        ApplyTheme(); // Zavolání metody pro aplikaci tématu při startu aplikace
    }

    private void ApplyTheme()
    {
        // Zjisti, zda je aktivní tmavý režim
        bool isDarkMode = IsDarkModeEnabled();

        // Vyber správný ResourceDictionary
        string theme = isDarkMode ? "Themes/Dark.xaml" : "Themes/Light.xaml";
        var dictionary = new ResourceDictionary
        {
            Source = new Uri(theme, UriKind.Relative)
        };

        // Aktualizuj zdroje aplikace
        Current.Resources.MergedDictionaries.Clear();
        Current.Resources.MergedDictionaries.Add(dictionary);
    }

    private bool IsDarkModeEnabled()
    {
        const string registryKeyPath = @"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize";
        const string registryValueName = "AppsUseLightTheme";

        using (var key = Registry.CurrentUser.OpenSubKey(registryKeyPath))
        {
            if (key != null && key.GetValue(registryValueName) is int value)
            {
                return value == 0; // 0 = Dark Mode, 1 = Light Mode
            }
        }
        return false; // Defaultně světlý režim
    }
}