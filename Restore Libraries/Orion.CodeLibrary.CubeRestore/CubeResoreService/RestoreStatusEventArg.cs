﻿using System;

namespace Orion.CodeLibrary.CubeReportsRestore
{
    public class RestoreStatus : EventArgs
    {
        public bool status { get; set; }
        public string errorInfo { get; set; }
    }
}