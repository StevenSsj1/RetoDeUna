from datetime import datetime
from collections import defaultdict
from datetime import timedelta

class AnalysisController:
    def __init__(self, transactions):
        self.transactions = transactions

    def analyze_transactions(self):
            
            month_translation = {
                "January": "Enero",
                "February": "Febrero",
                "March": "Marzo",
                "April": "Abril",
                "May": "Mayo",
                "June": "Junio",
                "July": "Julio",
                "August": "Agosto",
                "September": "Septiembre",
                "October": "Octubre",
                "November": "Noviembre",
                "December": "Diciembre"
            }

            current_date = datetime.utcnow()
            six_months_ago = current_date - timedelta(days=6*30)

            filtered_transactions = [
                transaction for transaction in self.transactions
                if datetime.fromisoformat(transaction["date"]) >= six_months_ago
            ]

            monthly_data = defaultdict(lambda: {"count": 0})
            for transaction in filtered_transactions:
                date = datetime.fromisoformat(transaction["date"])
                month = date.strftime("%B")
                month_spanish = month_translation[month]
                monthly_data[month_spanish]["count"] += 1
            
            chart_data = [{"month": month, "count": data["count"]} for month, data in monthly_data.items()]
            return chart_data

    def analyze_transactions(self, format: str = "month"):
        month_translation = {
            "January": "Enero",
            "February": "Febrero",
            "March": "Marzo",
            "April": "Abril",
            "May": "Mayo",
            "June": "Junio",
            "July": "Julio",
            "August": "Agosto",
            "September": "Septiembre",
            "October": "Octubre",
            "November": "Noviembre",
            "December": "Diciembre"
        }

        current_date = datetime.utcnow()
        six_months_ago = current_date - timedelta(days=6*30)

        filtered_transactions = [
            transaction for transaction in self.transactions
            if datetime.fromisoformat(transaction["date"]) >= six_months_ago
        ]

        if format == "month":
            monthly_data = defaultdict(lambda: {"count": 0})
            for transaction in filtered_transactions:
                date = datetime.fromisoformat(transaction["date"])
                month = date.strftime("%B")
                month_spanish = month_translation[month]
                monthly_data[month_spanish]["count"] += 1
            
            chart_data = [{"month": month, "count": data["count"]} for month, data in monthly_data.items()]
        elif format == "date":
            daily_data = defaultdict(lambda: {"count": 0})
            for transaction in filtered_transactions:
                date = datetime.fromisoformat(transaction["date"]).strftime("%Y-%m-%d")
                daily_data[date]["count"] += 1
            
            chart_data = [{"date": date, "count": data["count"]} for date, data in daily_data.items()]
        else:
            raise ValueError("Invalid format. Use 'month' or 'date'.")
            
        return chart_data

    def analyze_transactions_by_amount(self):
        month_translation = {
            "January": "Enero",
            "February": "Febrero",
            "March": "Marzo",
            "April": "Abril",
            "May": "Mayo",
            "June": "Junio",
            "July": "Julio",
            "August": "Agosto",
            "September": "Septiembre",
            "October": "Octubre",
            "November": "Noviembre",
            "December": "Diciembre"
        }
        current_date = datetime.utcnow()
        six_months_ago = current_date - timedelta(days=6*30)

        filtered_transactions = [
            transaction for transaction in self.transactions
            if datetime.fromisoformat(transaction["date"]) >= six_months_ago
        ]

        daily_data = defaultdict(lambda: {"amount": 0})
        for transaction in filtered_transactions:
            date = datetime.fromisoformat(transaction["date"]).strftime("%B")
            month_spanish = month_translation[date]
            daily_data[month_spanish]["amount"] += transaction["amount"]
        
        chart_data = [{"month": date, "amount": data["amount"]} for date, data in daily_data.items()]
        return chart_data