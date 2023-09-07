from django.shortcuts import render, redirect
import api

# Create your views here.

def redirect_index(request):
    return redirect("home", days_range=30, currencies="USD,CAD")
def dashboard(request, days_range=30, currencies="USD"):
    days, rates = api.get_rates(currencies=currencies.split(","), days=days_range)

    page_label = {7 : "Week", 30 : "Month", 365 : "Year"}.get(days_range, "Personalized")

    return render(request, 'devise/index.html', context={"data": rates,
                                                                      "days_labels": days,
                                                                      "currencies": currencies,
                                                                      "page_label" : page_label})