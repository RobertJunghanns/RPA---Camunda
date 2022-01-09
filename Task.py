from re import S
from pyzeebe import ZeebeTaskRouter
from googleAPI import send_mail

router = ZeebeTaskRouter()

@router.task(task_type="decrease_v_days")
async def decrease_v_days(remaining_v_days: int, requested_v_days: int) -> int:
    return {"remaining_v_days": remaining_v_days-requested_v_days}


@router.task(task_type="restore_v_days")
async def restore_v_days(remaining_v_days: int, requested_v_days: int) -> int:
    return {"remaining_v_days": remaining_v_days+requested_v_days}

@router.task(task_type="send_remainder_app")
async def send_remainder_app(sup_e_mail: str, applicant_name: str, requested_v_days: int, start_date: str):
    to = sup_e_mail
    subject = "Reminder Vacation Approval"
    text = f"""
Hello,

your employee {applicant_name} has submitted a vacation application for {requested_v_days} days from {start_date}. Please remember to approve your employee's vacation request.

Thank you!
    """

    send_mail(to=to, subject=subject, message_text=text)
    return