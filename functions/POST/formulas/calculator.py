""" This code executes:
1) calculate value cell
"""

class RPN:
    """
     RPN calculates value cell
    :return: new result sell
    """
    # ==========================================================================
    def is_op(symb):
        return symb in '+-*/'
    # ==========================================================================
    def prior( op ):
        match op:
            case '*' | '/':
                return 2
            case '+' | '-':
                return 1
    # ==========================================================================
    def __init__(self, expr):
        self.expr_lis = expr.split()
    #==========================================================================
    def check(self):
        return not RPN.is_op( self.expr_lis[-1] )
    # ==========================================================================
    def postfix(self):
        if self.check():
            try:
                out = []
                st  = []
                for symb in self.expr_lis:
                    if symb.isdigit():
                        out.append( symb )
                    elif symb == '(':
                        st.append( symb )
                    elif symb == ')':
                        if not st:
                            raise ValueError
                        while st and st[-1] != '(':
                            out.append( st.pop() )
                            if not st:
                                raise ValueError
                        st.pop()
                    elif RPN.is_op( symb ):
                        while st and RPN.is_op( st[-1] ) and RPN.prior( st[-1] ) >= RPN.prior( symb ):
                            out.append( st.pop() )
                        st.append( symb )
                while st:
                    out.append( st.pop() )
                return out
            except ValueError:
                print( 'Invalid expression specified.' )
        else:
            return self.expr_lis
    # ==========================================================================
    def calculate(self):
        self.expr_lis = self.postfix()
        st = []
        try:
            for symb in self.expr_lis:
                if symb.isdigit():
                    st.append( symb )
                elif RPN.is_op( symb ):
                    if not st:
                        raise ValueError
                    b = int( st.pop() )
                    if not st:
                        raise ValueError
                    a = int( st.pop() )
                    match symb:
                        case '+':
                            st.append( str(a + b) )
                        case '-':
                            st.append( str(a - b) )
                        case '*':
                            st.append( str(a * b) )
                        case '/':
                            st.append( str(a / b) )
            if len(st) != 1:
                raise ValueError
            return int( st.pop() )
        except ValueError:
            print( 'Invalid expression specified.' )
# =============================================================================
#rpn = RPN("( ( 34 - ( 5 + 2 ) ) * 3 ) * ( 1 + 7 ) ")
#print( rpn.check() )
#print( rpn.postfix() )
#print( rpn.calculate() )