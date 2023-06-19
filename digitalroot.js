function digitalRoot(n) {
  
    if (n == 0) {
        return 0;
      }
    else{
        return (n % 9) || 9;
    }
  
  }