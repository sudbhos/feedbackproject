from django import forms

from django.core import validators

# def start_with_s(value):
#     # if value[0].lower() != "s" and \
#     if value.isalpha()!=True:
#         raise forms.ValidationError("Its start with alpha only.")

class feedbackinfo(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(widget=forms.PasswordInput)
    feedback=forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(20),validators.MinLengthValidator(10)])

    def clean(self):
        print("Total Validataion.")
        cleaned_data = super().clean()
        inputname = cleaned_data['name']
        if len(inputname) < 9:
            raise forms.ValidationError("Please enter the value more than 9")
        inputrollno = cleaned_data["rollno"]
        if len(str(inputrollno)) != 3:
            raise forms.ValidationError("The lenght of file will 3 only.")

        inputpassword=cleaned_data["password"]
        inputrpassword=cleaned_data["rpassword"]
        if inputpassword !=inputrpassword:
            raise forms.ValidationError("Please enter the same password for both filed .")

#user define valideter
    # def clean_name(self):
    #     inputname=self.cleaned_data["name"]
    #     print("Validation name.")
    #     if len(inputname)<4:
    #         raise forms.ValidationError("The length is less than 4 , please enter the more than four lenth")
    #     return inputname
    # def clean_rollno(self):
    #     inputrollno=self.cleaned_data["rollno"]
    #     print("Roll no validation.")
    #     # if len(inputrollno)<4:
    #     #     raise forms.ValidationError("Please enter the length of rollno is 4 .")
    #     return inputrollno
    # def clean_email(self):
    #     inputemail=self.cleaned_data["email"]
    #     print("Validating email.")
    #     if len(str(inputemail))<6:
    #         raise forms.ValidationError("Length is less than 6.")
    #     return inputemail
    # def clean_feedback(self):
    #     inputfeedback=self.cleaned_data["feedback"]
    #     print("Validating feedback..")
    #     if len(inputfeedback)<10:
    #         raise forms.ValidationError("Please enter the value less than 10.")
    #     return inputfeedback