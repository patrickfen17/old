'Add Ticker, then volumne then Yearly change and Percent change
Sub Stock()

    'Track each row within the summary table
    Dim summary_row As Integer
    
    'Track each stock volume
    Dim total_volume As Double
    
    'Track opening stock price
    Dim opening_price As Double
    
    'Track the closing stock price
    Dim closing_price As Double
    
    'Track yearly change in stock price
    Dim yearly_change As Double
    
    'Track stock ticker symbol
    Dim ticker_symbol As String
    
    'Track Percent change in stock price
    Dim percent_change As Double
       
    'Loop through all woorksheets
    For Each ws In Worksheets
    
    'Set initial values for each variable
    summary_row = 2
    total_volume = 0
    opening_price = ws.Cells(2, 3)
    closing_price = 0
    lastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row
    percent_change = 0
    max_ticker = ""
    max_increase = 0
    min_ticker = ""
    min_increase = 99999999999#
    greatest_volume = 0
    greatest_ticker = ""
    
    'Setup summary table
    ws.Range("I1:Q1").Font.Bold = True
    ws.Range("I1").Value = "Ticker"
    ws.Range("J1").Value = "Yearly Change"
    ws.Range("K1").Value = "Percent Change"
    ws.Range("L1").Value = "Volume"
    ws.Columns(11).NumberFormat = "0.00%"
    ws.Columns(12).NumberFormat = "#,###,###,###"
    
    'Setup bonus table
    ws.Range("O2:O4").Font.Bold = True
    ws.Range("O2").Value = "Greatest % Increase"
    ws.Range("O3").Value = "Greatest % Decrease"
    ws.Range("O4").Value = "Greatest Total Volume"
    ws.Range("P1").Value = "Ticker"
    ws.Range("Q1").Value = "Value"
    ws.Range("Q4").NumberFormat = "#,###,###,###"
    
        'Loop through all rows in sheet
        For i = 2 To lastRow
        
        closing_price = ws.Cells(i, 6).Value
        total_volume = total_volume + ws.Cells(i, 7).Value
        
            If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1) Then
                
                ws.Cells(summary_row, 9).Value = ws.Cells(i, 1).Value
                ws.Cells(summary_row, 12).Value = total_volume
                yearly_change = closing_price - opening_price
                ws.Cells(summary_row, 10).Value = yearly_change
                
                If yearly_change > max_increase Then
                    max_increase = yearly_change
                    max_ticker = ws.Cells(i, 1).Value
                
                End If
                
                If yearly_change < min_increase Then
                    min_increase = yearly_change
                    min_ticker = ws.Cells(i, 1).Value
                
                End If
                
                If total_volume > greatest_volume Then
                    greatest_volume = total_volume
                    greatest_ticker = ws.Cells(i, 1).Value
                    
                End If
                
                If opening_price > 0 Then
                    percentage_change = yearly_change / opening_price
                    
                Else
                    percentage_change = 0
                            
                End If
                
                ws.Cells(summary_row, 11).Value = percentage_change
                
                    If yearly_change > 0 Then
                        ws.Cells(summary_row, 10).Interior.ColorIndex = 4
                        
                    ElseIf yearly_change < 0 Then
                        ws.Cells(summary_row, 10).Interior.ColorIndex = 3
                        
                    End If
                    
                summary_row = summary_row + 1
                total_volume = 0
                yearly_change = 0
                
                ws.Range("P2").Value = max_ticker
                ws.Range("Q2").Value = max_increase
                ws.Range("P3").Value = min_ticker
                ws.Range("Q3").Value = min_increase
                ws.Range("P4").Value = greatest_ticker
                ws.Range("Q4").Value = greatest_volume
               
    
           End If
        
        Next i
        ws.Range("I:Q").EntireColumn.AutoFit
    Next ws
    
End Sub

