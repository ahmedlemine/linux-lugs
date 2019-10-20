from django.shortcuts import render
from django.http import HttpResponse


#temp data
lugs = [
    {
        'added_by': 'Ahmed Lemine',
        'name': 'Dubai Linux Group',
        'city': 'Dubai',
        'country': 'UAE',
        'date_added': 'Sep 30, 2019',
        'description': 'Glen Barber has announced the release of the second of third release candidates for FreeBSD 12.1. The new development snapshot features relatively few changes as the 12.1 branch is nearing its stable launch. The release announcement lists the following adjustments since the first release candidate: "A summary of changes since 12.1-RC1 includes: The loader.efi had been updated to use ioalign for compliance with UEFI specification 2.7A. A null pointer dereference bug had been fixed. A fix to SCTP to reset local variables to their initial values had been added. The ixgbe(4) driver had been updated to prevent a system crash when configuring EEE on X500EM_X devices. The sdhci(4) driver had been updated to fix a boot issue on Beaglebone SoCs." Additional information on the 12.1'
    },
    {
        'added_by': 'Ahmed Lemine',
        'name': 'Madina Linux Group',
        'city': 'Madina',
        'country': 'KSA',
        'date_added': 'Sep 30, 2019',
        'description': 'Glen Barber has announced the release of the second of third release candidates for FreeBSD 12.1. The new development snapshot features relatively few changes as the 12.1 branch is nearing its stable launch. The release announcement lists the following adjustments since the first release candidate: "A summary of changes since 12.1-RC1 includes: The loader.efi had been updated to use ioalign for compliance with UEFI specification 2.7A. A null pointer dereference bug had been fixed. A fix to SCTP to reset local variables to their initial values had been added. The ixgbe(4) driver had been updated to prevent a system crash when configuring EEE on X500EM_X devices. The sdhci(4) driver had been updated to fix a boot issue on Beaglebone SoCs." Additional information on the 12.1'
    }


]

def home(request):
    context = {
        'lugs': lugs
    }
    return render(request, 'lugs/home.html', context)

def about(request):
    return render(request, 'lugs/about.html', {'title': 'About'})