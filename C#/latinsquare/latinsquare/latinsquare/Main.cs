using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace latinsquare
{
    public partial class Main : Form
    {
        public Main()
        {
            InitializeComponent();
            IsLatinSquare();
        }

        public void IsLatinSquare()
        {
            int length = 5;
            string[] input = "1 2 3 4 5 5 1 2 3 4 4 5 1 2 3 3 4 5 1 2 2 3 4 5 1".Split();
            int[] intput = Array.ConvertAll(input, s => int.Parse(s));

            int[,] matrix = new int[length, length];

            for (int i = 0; i < length; i++ )
            {
                matrix[i,length]
            }

        }
    }
}
