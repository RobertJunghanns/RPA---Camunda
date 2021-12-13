from pyzeebe import ZeebeTaskRouter

router = ZeebeTaskRouter()

@router.task(task_type="decrease_v_days")
async def decrease_v_days(remaining_v_days: int, requested_v_days: int) -> int:
    return {"remaining_v_days": remaining_v_days-requested_v_days}