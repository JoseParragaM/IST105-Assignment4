# calculator/views.py

from django.shortcuts import render
from .forms import InputForm
import math

def calculator_view(request):
    form = InputForm(request.POST or None)
    result = None
    error = None

    if request.method == 'POST':
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']

            if a < 1:
                error = "Value A is too small; it must be at least 1."
            elif c < 0:
                error = "Value C cannot be negative."
            else:
                note = ""
                if b == 0:
                    note = "Note: Value B is zero and will not affect the result. "
                cubed = c ** 3
                sqrt_cubed = math.sqrt(cubed)
                if cubed > 1000:
                    computed = sqrt_cubed * 10
                else:
                    computed = sqrt_cubed / a
                final_value = computed + b
                result = f"{note}{final_value}"
        else:
            error = "Please enter valid numeric values for A, B, and C."

    return render(request, 'calculator/result.html', {
        'form': form,
        'result': result,
        'error': error,
    })
